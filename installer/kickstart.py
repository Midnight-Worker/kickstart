#!/usr/bin/env python3
from __future__ import annotations

try:
    import curses
except ImportError:
    curses = None

import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

REPO_URL = "https://github.com/Midnight-Worker/kickstart.git"
CACHE_DIR = Path.home() / ".cache" / "installkickstart" / "repo"


def run(*args: str, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        check=True,
        text=True,
        capture_output=capture,
    )


def require(command: str) -> None:
    if shutil.which(command) is None:
        raise SystemExit(f"Fehler: '{command}' wurde nicht gefunden.")


def update_cache() -> None:
    CACHE_DIR.parent.mkdir(parents=True, exist_ok=True)

    if not (CACHE_DIR / ".git").exists():
        print("Kickstart-Repository wird einmalig geladen ...")
        run("git", "clone", "--filter=blob:none", "--no-checkout", REPO_URL, str(CACHE_DIR))
    else:
        print("Aktualisiere Branch-Liste ...")
        run("git", "-C", str(CACHE_DIR), "fetch", "--prune", "origin")


def get_branches() -> list[str]:
    result = run(
        "git",
        "-C",
        str(CACHE_DIR),
        "for-each-ref",
        "--format=%(refname:short)",
        "refs/remotes/origin",
        capture=True,
    )

    branches = []
    for line in result.stdout.splitlines():
        if line == "origin/HEAD":
            continue
        if line.startswith("origin/"):
            branches.append(line.removeprefix("origin/"))

    return sorted(branches, key=str.lower)


def choose_branch_curses(branches: list[str]) -> str:
    if curses is None:
        raise RuntimeError("curses ist nicht verfügbar.")

    def menu(stdscr: curses.window) -> str:
        curses.curs_set(0)
        stdscr.keypad(True)

        selected = 0
        offset = 0

        while True:
            height, width = stdscr.getmaxyx()
            visible = max(1, height - 4)

            if selected < offset:
                offset = selected
            elif selected >= offset + visible:
                offset = selected - visible + 1

            stdscr.erase()
            stdscr.addnstr(0, 0, "Kickstart auswählen", width - 1, curses.A_BOLD)
            stdscr.addnstr(
                1,
                0,
                "↑/↓ wählen · Enter bestätigen · q abbrechen",
                width - 1,
            )

            for row, branch in enumerate(branches[offset:offset + visible], start=3):
                index = offset + row - 3
                marker = "> " if index == selected else "  "
                attr = curses.A_REVERSE if index == selected else curses.A_NORMAL
                stdscr.addnstr(row, 0, marker + branch, width - 1, attr)

            stdscr.refresh()
            key = stdscr.getch()

            if key in (curses.KEY_UP, ord("k")):
                selected = (selected - 1) % len(branches)
            elif key in (curses.KEY_DOWN, ord("j")):
                selected = (selected + 1) % len(branches)
            elif key in (10, 13, curses.KEY_ENTER):
                return branches[selected]
            elif key in (ord("q"), 27):
                raise KeyboardInterrupt

    return curses.wrapper(menu)


def choose_branch_fallback(branches: list[str]) -> str:
    for index, branch in enumerate(branches, start=1):
        print(f"{index:2}. {branch}")

    while True:
        value = input("Nummer: ").strip()
        if value.isdigit() and 1 <= int(value) <= len(branches):
            return branches[int(value) - 1]
        print("Ungültige Auswahl.")


def safe_directory_name(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9._ -]+", value)) and value not in {".", ".."}


def ask_destination(branch: str) -> Path:
    default = branch.replace("/", "-")

    while True:
        value = input(f"Verzeichnisname [{default}]: ").strip() or default

        if not safe_directory_name(value):
            print("Bitte nur Buchstaben, Zahlen, Leerzeichen, Punkt, Minus oder Unterstrich verwenden.")
            continue

        destination = Path.cwd() / value

        if destination.exists():
            print(f"'{destination}' existiert bereits.")
            continue

        return destination


def validate_member(destination: Path, member: tarfile.TarInfo) -> None:
    target = (destination / member.name).resolve()
    base = destination.resolve()

    if target != base and base not in target.parents:
        raise RuntimeError(f"Unsicherer Archivpfad: {member.name}")


def export_branch(branch: str, destination: Path) -> None:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(CACHE_DIR),
            "archive",
            "--format=tar",
            f"origin/{branch}",
        ],
        check=True,
        stdout=subprocess.PIPE,
    )

    destination.mkdir(parents=True)

    try:
        with tarfile.open(fileobj=io.BytesIO(result.stdout), mode="r:") as archive:
            for member in archive.getmembers():
                validate_member(destination, member)
            archive.extractall(destination)
    except Exception:
        shutil.rmtree(destination, ignore_errors=True)
        raise


def main() -> int:
    require("git")
    update_cache()

    branches = get_branches()
    if not branches:
        raise SystemExit("Keine Branches gefunden.")

    try:
        branch = choose_branch_curses(branches)
    except RuntimeError:
        branch = choose_branch_fallback(branches)
    except Exception as error:
        if curses is not None and isinstance(error, curses.error):
            branch = choose_branch_fallback(branches)
        else:
            raise
    except KeyboardInterrupt:
        print("\nAbgebrochen.")
        return 130

    print(f"\nGewählt: {branch}")
    destination = ask_destination(branch)

    print(f"Erzeuge {destination.name} ...")
    export_branch(branch, destination)

    print()
    print("Fertig:")
    print(f"  {destination}")
    print()
    print("Start:")
    print(f'  cd "{destination}"')

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as error:
        print(f"Ein Befehl ist fehlgeschlagen: {error}", file=sys.stderr)
        raise SystemExit(error.returncode)

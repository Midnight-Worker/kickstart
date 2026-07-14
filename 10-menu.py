#/c/Users/maikt/.ipython/profile_default/startup/10-menu.py

from __future__ import annotations

import asyncio
import subprocess
from pathlib import Path
from typing import Any

import win32com.client as win32
from IPython.core.magic import register_line_magic
from playwright.async_api import async_playwright


BASH = r"C:\msys64\usr\bin\bash.exe"

DEFAULT_URL = "https://quotes.toscrape.com/"


def _ipython():
    return get_ipython()


def _put(**objects: Any) -> None:
    """Objekte im globalen IPython-Namensraum ablegen."""
    _ipython().user_ns.update(objects)


def _get(name: str, default=None):
    return _ipython().user_ns.get(name, default)


def _dialog_menu() -> str:
    script = r'''
dialog \
    --stdout \
    --clear \
    --title "IPython-Werkbank" \
    --menu "Was möchtest du öffnen?" \
    20 70 12 \
    playwright "Chromium mit Playwright starten" \
    savehtml   "Aktuelle Seite als index.html speichern" \
    excel      "Microsoft Excel öffnen" \
    word       "Microsoft Word öffnen" \
    access     "Microsoft Access öffnen" \
    outlook    "Klassisches Outlook öffnen" \
    office     "Excel, Word und Outlook gemeinsam öffnen" \
    objects    "Verfügbare Steuerobjekte anzeigen" \
    closeweb   "Playwright-Browser schließen" \
    closeoffice "Office-Programme schließen" \
    files      "Dateien im aktuellen Ordner anzeigen" \
    exit       "IPython verlassen"
'''

    result = subprocess.run(
        [BASH, "-lc", script],
        stdout=subprocess.PIPE,
        stderr=None,
        text=True,
        check=False,
    )

    return result.stdout.strip()


async def start_browser(
    url: str = DEFAULT_URL,
    headless: bool = False,
):
    pw = await async_playwright().start()

    browser = await pw.chromium.launch(
        headless=headless,
    )

    page = await browser.new_page()
    await page.goto(
        url,
        wait_until="domcontentloaded",
    )

    return pw, browser, page


async def stop_browser(pw, browser) -> None:
    if browser is not None and browser.is_connected():
        await browser.close()

    if pw is not None:
        await pw.stop()


async def _start_browser_and_export() -> None:
    old_browser = _get("browser")

    if old_browser is not None and old_browser.is_connected():
        print("Playwright läuft bereits.")
        print("Objekte: pw, browser, page")
        return

    print("Chromium wird gestartet …")

    try:
        pw, browser, page = await start_browser()

        _put(
            pw=pw,
            browser=browser,
            page=page,
        )

        print("Playwright ist bereit.")
        print("Objekte: pw, browser, page")
        print()
        print("Beispiele:")
        print("  await page.title()")
        print("  page.url")
        print('  await page.goto("https://example.com/")')
        print("  html = await page.content()")

    except Exception as error:
        print(f"Playwright konnte nicht gestartet werden: {error}")


async def _save_html() -> None:
    page = _get("page")

    if page is None:
        print("Es existiert noch kein page-Objekt.")
        print("Starte zuerst Playwright.")
        return

    if page.is_closed():
        print("Der Browser-Tab ist bereits geschlossen.")
        return

    html = await page.content()
    path = Path.cwd() / "index.html"

    path.write_text(
        html,
        encoding="utf-8",
    )

    _put(html=html)

    print(f"Gespeichert: {path}")
    print("Variable verfügbar: html")


async def _close_browser_objects() -> None:
    pw = _get("pw")
    browser = _get("browser")

    if pw is None and browser is None:
        print("Keine Playwright-Sitzung vorhanden.")
        return

    try:
        await stop_browser(pw, browser)
    finally:
        _put(
            pw=None,
            browser=None,
            page=None,
        )

    print("Playwright wurde geschlossen.")


def open_excel() -> None:
    excel = _get("excel")

    if excel is None:
        excel = win32.DispatchEx("Excel.Application")
        excel.Visible = True

        book = excel.Workbooks.Add()
        sheet = book.Worksheets(1)

        _put(
            excel=excel,
            book=book,
            sheet=sheet,
        )

    else:
        excel.Visible = True

    print("Excel ist bereit.")
    print("Objekte: excel, book, sheet")
    print('Beispiel: sheet.Range("A1").Value = "Hallo"')


def open_word() -> None:
    word = _get("word")

    if word is None:
        word = win32.DispatchEx("Word.Application")
        word.Visible = True

        document = word.Documents.Add()

        _put(
            word=word,
            document=document,
        )

    else:
        word.Visible = True

    print("Word ist bereit.")
    print("Objekte: word, document")
    print('Beispiel: document.Content.Text = "Hallo aus IPython"')


def open_access() -> None:
    access = _get("access")

    if access is None:
        access = win32.DispatchEx("Access.Application")
        access.Visible = True

        _put(access=access)

    else:
        access.Visible = True

    print("Access ist bereit.")
    print("Objekt: access")
    print(
        'Datenbank öffnen:\n'
        'access.OpenCurrentDatabase(r"C:\\Pfad\\daten.accdb")'
    )


def open_outlook() -> None:
    outlook = _get("outlook")

    if outlook is None:
        outlook = win32.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")

        _put(
            outlook=outlook,
            outlook_namespace=namespace,
        )

    print("Outlook ist bereit.")
    print("Objekte: outlook, outlook_namespace")
    print()
    print("Neue E-Mail:")
    print("  mail = outlook.CreateItem(0)")
    print('  mail.Subject = "Test"')
    print('  mail.Body = "Hallo aus IPython"')
    print("  mail.Display()")


def show_objects() -> None:
    names = [
        "pw",
        "browser",
        "page",
        "html",
        "excel",
        "book",
        "sheet",
        "word",
        "document",
        "access",
        "outlook",
        "outlook_namespace",
    ]

    print()
    print("IPython-Steuerobjekte")
    print("-" * 40)

    for name in names:
        value = _get(name)

        if value is not None:
            print(f"{name:20} {type(value).__name__}")


def show_files() -> None:
    print()
    print(Path.cwd())
    print("-" * 40)

    for path in sorted(Path.cwd().iterdir()):
        suffix = "/" if path.is_dir() else ""
        print(f"{path.name}{suffix}")


def close_office() -> None:
    book = _get("book")
    excel = _get("excel")
    document = _get("document")
    word = _get("word")
    access = _get("access")

    try:
        if book is not None:
            book.Close(SaveChanges=False)
    except Exception as error:
        print(f"Excel-Arbeitsmappe: {error}")

    try:
        if excel is not None:
            excel.Quit()
    except Exception as error:
        print(f"Excel: {error}")

    try:
        if document is not None:
            document.Close(SaveChanges=False)
    except Exception as error:
        print(f"Word-Dokument: {error}")

    try:
        if word is not None:
            word.Quit()
    except Exception as error:
        print(f"Word: {error}")

    try:
        if access is not None:
            access.Quit()
    except Exception as error:
        print(f"Access: {error}")

    _put(
        excel=None,
        book=None,
        sheet=None,
        word=None,
        document=None,
        access=None,
    )

    print("Excel, Word und Access wurden geschlossen.")
    print("Outlook wird absichtlich nicht automatisch beendet.")


async def save_current_html(
    filename: str = "index.html",
) -> None:
    page = _get("page")

    if page is None:
        print("Kein page-Objekt vorhanden.")
        print("Starte zuerst Playwright.")
        return

    if page.is_closed():
        print("Der Browser-Tab ist geschlossen.")
        return

    html = await page.content()
    path = Path(filename).resolve()

    path.write_text(
        html,
        encoding="utf-8",
    )

    _put(html=html)

    print(f"HTML gespeichert: {path}")
    print("Variable verfügbar: html")


async def stop_current_browser() -> None:
    pw = _get("pw")
    browser = _get("browser")

    if browser is None and pw is None:
        print("Keine Playwright-Sitzung vorhanden.")
        return

    try:
        if browser is not None and browser.is_connected():
            await browser.close()

        if pw is not None:
            await pw.stop()

    finally:
        _put(
            pw=None,
            browser=None,
            page=None,
        )

    print("Playwright wurde beendet.")


@register_line_magic
def q(line: str) -> None:
    choice = _dialog_menu()
    ip = get_ipython()

    if choice == "playwright":
        ip.set_next_input(
            "pw, browser, page = await start_browser()",
            replace=True,
        )

    elif choice == "savehtml":
        ip.set_next_input(
            "await save_current_html()",
            replace=True,
        )

    elif choice == "closeweb":
        ip.set_next_input(
            "await stop_current_browser()",
            replace=True,
        )

    elif choice == "excel":
        open_excel()

    elif choice == "word":
        open_word()

    elif choice == "access":
        open_access()

    elif choice == "outlook":
        open_outlook()

    elif choice == "office":
        open_excel()
        open_word()
        open_outlook()

    elif choice == "objects":
        show_objects()

    elif choice == "closeoffice":
        close_office()

    elif choice == "files":
        show_files()

    elif choice == "exit":
        ip.ask_exit()


del q

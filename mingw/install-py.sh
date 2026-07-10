#!/usr/bin/env bash
set -euo pipefail

PY_VER="3.13.13"
PY_ARCH="amd64"
INSTALL_DIR="$HOME/install-cache"

mkdir -p "$INSTALL_DIR"

PY_FILE="python-${PY_VER}-${PY_ARCH}.exe"
PY_URL="https://www.python.org/ftp/python/${PY_VER}/${PY_FILE}"
PY_PATH="${INSTALL_DIR}/${PY_FILE}"

echo "==> Lade Python ${PY_VER} herunter..."
curl -fL --retry 3 -o "$PY_PATH" "$PY_URL"

echo "==> Prüfe, ob Datei vorhanden ist..."
ls -lh "$PY_PATH"

echo "==> Starte Python-Installer..."
MSYS2_ARG_CONV_EXCL='*' "$PY_PATH" \
  /quiet \
  InstallAllUsers=0 \
  PrependPath=1 \
  Include_launcher=1 \
  Include_pip=1 \
  Include_test=0

echo "==> Python-Installation angestoßen/abgeschlossen."

echo "==> Teste Python über py launcher..."
cmd.exe /c "py --version"

echo "==> Fertig."

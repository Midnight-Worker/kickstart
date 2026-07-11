#!/usr/bin/env bash
set -euo pipefail

APP_DIR="${HOME}/.local/share/installkickstart"
BIN_DIR="${HOME}/.local/bin"
BASHRC="${HOME}/.bashrc"
RAW_BASE="https://raw.githubusercontent.com/Midnight-Worker/kickstart/main/installer"

mkdir -p "$APP_DIR" "$BIN_DIR"

echo "Installiere installkickstart ..."

if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$RAW_BASE/kickstart.py" -o "$APP_DIR/kickstart.py"
elif command -v wget >/dev/null 2>&1; then
    wget -qO "$APP_DIR/kickstart.py" "$RAW_BASE/kickstart.py"
else
    echo "Fehler: curl oder wget wird benötigt." >&2
    exit 1
fi

cat > "$BIN_DIR/installkickstart" <<EOF
#!/usr/bin/env bash
exec python "$APP_DIR/kickstart.py" "\$@"
EOF

chmod +x "$BIN_DIR/installkickstart"

MARKER="# installkickstart"
if ! grep -Fq "$MARKER" "$BASHRC" 2>/dev/null; then
    cat >> "$BASHRC" <<'EOF'

# installkickstart
export PATH="$HOME/.local/bin:$PATH"
alias ik="installkickstart"
EOF
fi

echo
echo "Fertig."
echo "Aktiviere den Befehl jetzt mit:"
echo
echo "    source ~/.bashrc"
echo
echo "Danach:"
echo
echo "    installkickstart"
echo
echo "Kurzer Alias:"
echo
echo "    ik"

#!/usr/bin/env bash

# ============================================================
# Midnight Worker – Entwicklungsumgebung
# Wird gestartet mit:
# wget -qO- URL | bash
# ============================================================

TITLE="Midnight Worker Kickstart"
BACKTITLE="Installation der Entwicklungsumgebung"

# Farben für dialog aktivieren
export DIALOGRC="${DIALOGRC:-}"

# ------------------------------------------------------------
# Voraussetzungen prüfen
# ------------------------------------------------------------

if ! command -v dialog >/dev/null 2>&1; then
    echo "Fehler: dialog wurde nicht gefunden."
    echo
    read -rp "Enter drücken ..." </dev/tty
    exit 1
fi

# ------------------------------------------------------------
# Hauptauswahl
# ------------------------------------------------------------

auswahl=$(
    dialog \
        --stdout \
        --separate-output \
        --backtitle "$BACKTITLE" \
        --title "$TITLE" \
        --checklist \
        "Wähle die Komponenten aus.\n\nLeertaste: auswählen\nEnter: bestätigen" \
        22 74 12 \
        "qt"       "Qt6 und QML6"                    off \
        "compiler" "MinGW C/C++ Compiler und Make"  off \
        "python"   "Python und pip"                 off \
        "nodejs"   "Node.js und npm"                off \
        "editors"  "Editoren: Vim und Nano"         off \
        "explorer" "Dateimanager: vifm und lf"      off \
        </dev/tty
)

status=$?

# Abbrechen wurde gedrückt
if [[ $status -ne 0 ]]; then
    clear
    echo "Installation abgebrochen."
    exit 0
fi

# Keine Auswahl getroffen
if [[ -z "$auswahl" ]]; then
    dialog \
        --backtitle "$BACKTITLE" \
        --title "Keine Auswahl" \
        --msgbox "Es wurden keine Komponenten ausgewählt." \
        8 50 \
        </dev/tty

    clear
    exit 0
fi

# ------------------------------------------------------------
# Auswahl zur Kontrolle anzeigen
# ------------------------------------------------------------

anzeige=""

while IFS= read -r paket; do
    case "$paket" in
        qt)
            anzeige+="• Qt6 und QML6\n"
            ;;
        compiler)
            anzeige+="• MinGW C/C++ Compiler und Make\n"
            ;;
        python)
            anzeige+="• Python und pip\n"
            ;;
        nodejs)
            anzeige+="• Node.js und npm\n"
            ;;
        editors)
            anzeige+="• Vim und Nano\n"
            ;;
        explorer)
            anzeige+="• vifm und lf\n"
            ;;
    esac
done <<< "$auswahl"

dialog \
    --backtitle "$BACKTITLE" \
    --title "Auswahl bestätigen" \
    --yesno \
    "Folgende Komponenten werden installiert:\n\n${anzeige}\nInstallation jetzt starten?" \
    18 64 \
    </dev/tty

if [[ $? -ne 0 ]]; then
    clear
    echo "Installation abgebrochen."
    exit 0
fi

# ------------------------------------------------------------
# Installationsfunktionen
# Die Befehle können später angepasst werden.
# ------------------------------------------------------------

install_qt()
{
    echo
    echo "========================================"
    echo " Installiere Qt6 und QML6"
    echo "========================================"

    pacman -S --needed --noconfirm \
        mingw-w64-ucrt-x86_64-qt6-base \
        mingw-w64-ucrt-x86_64-qt6-declarative
}

install_compiler()
{
    echo
    echo "========================================"
    echo " Installiere Compiler und Make"
    echo "========================================"

    pacman -S --needed --noconfirm \
        mingw-w64-ucrt-x86_64-gcc \
        mingw-w64-ucrt-x86_64-gdb \
        mingw-w64-ucrt-x86_64-make \
        make
}

install_python()
{
    echo
    echo "========================================"
    echo " Installiere Python und pip"
    echo "========================================"

    pacman -S --needed --noconfirm \
        mingw-w64-ucrt-x86_64-python \
        mingw-w64-ucrt-x86_64-python-pip
}

install_nodejs()
{
    echo
    echo "========================================"
    echo " Installiere Node.js und npm"
    echo "========================================"

    pacman -S --needed --noconfirm \
        mingw-w64-ucrt-x86_64-nodejs \
        mingw-w64-ucrt-x86_64-npm
}

install_editors()
{
    echo
    echo "========================================"
    echo " Installiere Vim und Nano"
    echo "========================================"

    pacman -S --needed --noconfirm \
        vim \
        nano
}

install_explorer()
{
    echo
    echo "========================================"
    echo " Installiere vifm und lf"
    echo "========================================"

    pacman -S --needed --noconfirm \
        vifm \
        lf
}

# ------------------------------------------------------------
# Installation durchführen
# ------------------------------------------------------------

clear

echo "Midnight Worker Kickstart"
echo "Installation wird gestartet ..."

while IFS= read -r paket; do
    case "$paket" in
        qt)
            install_qt
            ;;
        compiler)
            install_compiler
            ;;
        python)
            install_python
            ;;
        nodejs)
            install_nodejs
            ;;
        editors)
            install_editors
            ;;
        explorer)
            install_explorer
            ;;
    esac
done <<< "$auswahl"

# ------------------------------------------------------------
# Abschluss
# ------------------------------------------------------------

dialog \
    --backtitle "$BACKTITLE" \
    --title "Installation abgeschlossen" \
    --msgbox \
    "Die ausgewählten Installationsschritte wurden ausgeführt.\n\nGit Bash kann jetzt geschlossen werden." \
    10 62 \
    </dev/tty

clear

echo "========================================"
echo " Installation abgeschlossen"
echo "========================================"
echo

read -rp "Enter drücken, um Git Bash zu schließen ..." </dev/tty

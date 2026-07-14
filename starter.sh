#!/usr/bin/env bash

# Auswahl anzeigen und Ergebnis speichern
auswahl=$(dialog \
    --stdout \
    --clear \
    --title "Terminal-Starter" \
    --menu "Was möchtest du starten?" \
    16 60 6 \
    bash    "Normale Bash verwenden" \
    ipython "Interaktive Python-Shell" \
    ranger  "Dateimanager starten" \
    vim     "Vim mit NERDTree starten" \
    exit    "Terminal schließen"
)

# Terminal nach dialog aufräumen
clear

case "$auswahl" in
    bash)
        # Nichts starten – wir befinden uns bereits in Bash
        ;;

    ipython)
        python -m IPython
        ;;

    ranger)
        lf
        ;;

    vim)
        vim -c "NERDTreeToggle"
        ;;

    exit)
        exit
        ;;

    "")
        # Escape oder Abbrechen
        echo "Startmenü abgebrochen."
        ;;
esac

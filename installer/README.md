# installkickstart

Minimaler interaktiver Projektgenerator für die Branches von:

https://github.com/Midnight-Worker/kickstart

## Dateien im Repository ablegen

```text
kickstart/
└── installer/
    ├── install.sh
    └── kickstart.py
```

## Installation aus GitHub

```bash
curl -fsSL https://raw.githubusercontent.com/Midnight-Worker/kickstart/main/installer/install.sh | bash
source ~/.bashrc
```

Alternativ mit wget:

```bash
wget -qO- https://raw.githubusercontent.com/Midnight-Worker/kickstart/main/installer/install.sh | bash
source ~/.bashrc
```

## Verwendung

```bash
installkickstart
```

oder kurz:

```bash
ik
```

Das Tool:

1. hält einen Cache unter `~/.cache/installkickstart/repo`,
2. aktualisiert die Remote-Branches,
3. zeigt sie in einem curses-Menü,
4. exportiert den gewählten Branch mit `git archive`,
5. erzeugt dadurch ein frisches Verzeichnis ohne `.git`.

## Voraussetzungen

- Bash
- Python 3
- Git
- curl oder wget nur für die Erstinstallation

Geeignet für:

- Linux
- WSL
- Git Bash
- MSYS2 Bash

Unter einer normalen Windows-CMD funktioniert das Bash-Installationsskript nicht.

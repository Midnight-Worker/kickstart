# Hilfe zu einem Objekt
page.goto?
soup.find_all?

# Ausführlichere Hilfe / Quellcode
page.goto??
soup.find_all??

# Variablen anzeigen
%who
%whos

# Verlauf anzeigen
%history
%history -n

# Letzte Befehle in Datei speichern
%save session.py 1-20

# Python-Datei ausführen
%run scraper.py

# Datei nach Änderungen erneut ausführen
%run scraper.py

# Arbeitsverzeichnis anzeigen
%pwd

# Verzeichnis wechseln
%cd /pfad/zum/projekt

# Dateien anzeigen
%ls

# Shell-Befehl ausführen
!ls -la
!cat index.html
!sqlite3 daten.db

# Zeit messen
%time soup.select("a")
%timeit soup.select("a")

# Variable löschen
del html

# Alle eigenen Variablen löschen
%reset

# IPython verlassen
exit

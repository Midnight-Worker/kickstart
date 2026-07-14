## Die wichtigsten Regex-Zeichen

    ^ Zeilenanfang  
    $ Zeilenende  
    . genau ein beliebiges Zeichen  
    * vorheriges Muster 0-mal oder öfter  
    + vorheriges Muster 1-mal oder öfter  
    ? vorheriges Muster 0-mal oder 1-mal  
    [] genau ein Zeichen aus einer Auswahl  
    [^] genau ein Zeichen, das nicht in der Auswahl ist  
    () Gruppe  
    | oder  
    {} genaue Anzahl oder Bereich  
    \ Sonderzeichen maskieren

------------------------------------------------------------------------

# Zeilenanfang und Zeilenende

## `^` -- Zeilenanfang

Alle Zeilen, die mit `Maik` beginnen:

    grep '^Maik' users.csv

Passt auf:

    Maik;Oer-Erkenschwick;45

Passt nicht auf:

    1;Maik;Oer-Erkenschwick;45

## `$` -- Zeilenende

Alle Zeilen, die mit `yes` enden:

    grep 'yes$' users.csv

Bei deiner CSV besser genauer:

    grep ';yes$' users.csv

Damit muss wirklich das letzte Feld `yes` sein.

## Ganze Zeile prüfen

    grep '^Maik$' names.txt

Das passt nur auf eine Zeile, die exakt aus `Maik` besteht.

Nicht auf:

    Maik TappeHallo MaikMaik123

------------------------------------------------------------------------

# Der Punkt `.`

Der Punkt steht für genau ein beliebiges Zeichen.

    M.ik

Passt auf:

    MaikMeikM3ikM-ik

Der Punkt bedeutet nicht wirklich einen Punkt.

Für einen echten Punkt:

    \.

Beispiel:

    grep '\.txt$' files.txt

Findet Dateinamen, die auf `.txt` enden.

------------------------------------------------------------------------

# Der Stern `*`

`*` bedeutet:

    Das vorherige Zeichen oder Muster darf 0-mal oder beliebig oft vorkommen.

    ab*c

Passt auf:

    acabcabbcabbbbbc

Denn das `b` darf fehlen oder beliebig oft vorkommen.

Wichtig:

    .*

bedeutet:

    beliebig viele beliebige Zeichen

Beispiel:

    ^Maik.*Berlin$

Bedeutet:

    Zeile beginnt mit Maikdanach kommt irgendetwasZeile endet mit Berlin

------------------------------------------------------------------------

# Das Plus `+`

`+` bedeutet:

    Das vorherige Muster muss mindestens einmal vorkommen.

    ab+c

Passt auf:

    abcabbcabbbbbc

Passt nicht auf:

    ac

Bei `grep` brauchst du dafür meistens erweitertes Regex:

    grep -E 'ab+c' datei.txt

Oder:

    egrep 'ab+c' datei.txt

`grep -E` ist heute die klarere Schreibweise.

------------------------------------------------------------------------

# Das Fragezeichen `?`

`?` bedeutet:

    Das vorherige Muster ist optional.

    colou?r

Passt auf:

    colorcolour

Mit `grep`:

    grep -E 'colou?r' datei.txt

Ein praktisches deutsches Beispiel:

    Straße?

Hier wäre nur das letzte `e` optional:

    StraßStraße

Für ganze Wörter braucht man Gruppen:

    Straß(e)?

------------------------------------------------------------------------

# Zeichenklassen `[]`

## Eine Auswahl erlauben

    [abc]

Passt auf genau eines dieser Zeichen:

    abc

Beispiel:

    M[ae]ik

Passt auf:

    MaikMeik

## Bereiche

    [0-9]

Eine Ziffer.

    [a-z]

Ein Kleinbuchstabe.

    [A-Z]

Ein Großbuchstabe.

    [a-zA-Z]

Ein Buchstabe.

    [a-zA-Z0-9]

Ein Buchstabe oder eine Ziffer.

------------------------------------------------------------------------

# Negierte Zeichenklassen `[^...]`

Das `^` innerhalb einer Zeichenklasse bedeutet nicht Zeilenanfang, sondern:

    alles außer

    [^0-9]

Passt auf ein Zeichen, das keine Ziffer ist.

    [^;]+

Bedeutet:

    ein oder mehrere Zeichen, die kein Semikolon sind

Das ist für deine CSV-Dateien sehr nützlich.

Beispiel:

    ^[^;]+;[^;]+;[^;]+$

Das beschreibt grob eine Zeile mit drei Feldern, getrennt durch Semikolons.

------------------------------------------------------------------------

# Wiederholungen mit `{}`

Mit erweitertem Regex:

    [0-9]{4}

Genau vier Ziffern.

    grep -E '[0-9]{4}' datei.txt

Beispiele:

    202647111234

## Mindestens

    [0-9]{2,}

Mindestens zwei Ziffern.

## Bereich

    [0-9]{2,5}

Zwischen zwei und fünf Ziffern.

## Genau eine deutsche Postleitzahl

    ^[0-9]{5}$

------------------------------------------------------------------------

# Gruppen `()`

Gruppen fassen Muster zusammen.

    (Hallo)+

Passt auf:

    HalloHalloHalloHalloHalloHallo

Mit `grep`:

    grep -E '(Hallo)+' datei.txt

Praktischer:

    ^(Herr|Frau) 

Bedeutet:

    Zeile beginnt mit Herr oder Frau, gefolgt von einem Leerzeichen

------------------------------------------------------------------------

# Oder `|`

    Berlin|Dortmund|Bochum

Findet eine dieser Städte:

    grep -E 'Berlin|Dortmund|Bochum' users.csv

Mit genauem Feld:

    grep -E ';(Berlin|Dortmund|Bochum);' users.csv

------------------------------------------------------------------------

# Wortgrenzen

## `\b`

`\b` steht häufig für eine Wortgrenze.

In Python:

    r"\bcat\b"

Passt auf:

    catthe cat sleeps

Passt nicht auf:

    categorybobcat

Bei GNU `grep` kannst du auch verwenden:

    grep -E '\bcat\b' datei.txt

Noch einfacher bei `grep`:

    grep -w 'cat' datei.txt

`-w` bedeutet: vollständiges Wort.

------------------------------------------------------------------------

# Häufige Kurzformen

Diese sind besonders in Python und vielen modernen Regex-Varianten wichtig:

    \d Ziffer  
    \D keine Ziffer  
    \w Buchstabe, Ziffer oder Unterstrich  
    \W kein Wortzeichen  
    \s Leerzeichen, Tab oder Zeilenumbruch  
    \S kein Leerraum

Beispiele:

    \d+

Eine oder mehrere Ziffern.

    \w+

Ein oder mehrere Wortzeichen.

    \s+

Ein oder mehrere Leerraumzeichen.

In Python:

    import re  
      
    text = "Alter: 45"  
      
    match = re.search(r"\d+", text)  
      
    if match:  
    print(match.group())

Ausgabe:

    45

Bei klassischem `grep` funktionieren diese Kurzformen nicht immer gleich zuverlässig. Für Shell-Skripte ist häufig sicherer:

    [0-9]

statt:

    \d

------------------------------------------------------------------------

# Leerzeichen

Ein normales Leerzeichen kannst du direkt schreiben:

    Maik Tappe

Beliebig viele Leerzeichen oder Tabs:

    [[:space:]]+

Mit `grep -E`:

    grep -E 'Maik[[:space:]]+Tappe' datei.txt

POSIX-Zeichenklassen sind für `grep`, `sed` und `awk` besonders nützlich:

    [[:digit:]] Ziffer  
    [[:alpha:]] Buchstabe  
    [[:alnum:]] Buchstabe oder Ziffer  
    [[:space:]] Leerraum  
    [[:lower:]] Kleinbuchstabe  
    [[:upper:]] Großbuchstabe

Beispiel:

    grep -E '^[[:digit:]]+$' datei.txt

Findet Zeilen, die nur aus Ziffern bestehen.

------------------------------------------------------------------------

# Sonderzeichen maskieren

Diese Zeichen haben in Regex eine Sonderbedeutung:

    . ^ $ * + ? ( ) [ ] { } | \

Willst du sie wörtlich suchen, musst du meist einen Backslash verwenden.

Echter Punkt:

    \.

Echtes Plus:

    \+

Echte Klammer:

    \(

Beispiel Telefonnummer:

    ^\+49

Findet Zeilen, die mit `+49` beginnen.

------------------------------------------------------------------------

# Besonders wichtige Praxisbeispiele

## Leere Zeilen finden

    ^$

    grep '^$' datei.txt

Leere Zeilen entfernen:

    sed '/^$/d' datei.txt

## Zeilen mit nur Leerzeichen

    ^[[:space:]]*$

    grep -E '^[[:space:]]*$' datei.txt

Entfernen:

    sed -E '/^[[:space:]]*$/d' datei.txt

## Kommentarzeilen finden

    ^#

    grep '^#' config.txt

Kommentare und Leerzeilen entfernen:

    grep -Ev '^[[:space:]]*(#|$)' config.txt

Das bedeutet:

    ^ Zeilenanfang  
    [[:space:]]* beliebig viel Leerraum  
    (#|$) dann Kommentarzeichen oder direkt Zeilenende

------------------------------------------------------------------------

# CSV-Beispiele

Angenommen:

    1;Maik;Oer-Erkenschwick;45;yes  
    2;Anna;Dortmund;31;yes  
    3;Tom;Bochum;17;no

## Aktive Benutzer

    grep ';yes$' users.csv

## Inaktive Benutzer

    grep ';no$' users.csv

## Benutzer aus Dortmund

    grep ';Dortmund;' users.csv

## Zeilen, die mit einer ID beginnen

    grep -E '^[0-9]+;' users.csv

## Zeilen mit einer zweistelligen Altersangabe

    grep -E ';[0-9]{2};' users.csv

## E-Mail-Adressen grob erkennen

    ^[^@[:space:]]+@[^@[:space:]]+\.[^@[:space:]]+$

Das ist keine perfekte E-Mail-Prüfung, aber für Übungen brauchbar.

------------------------------------------------------------------------

# Suchen und ersetzen mit `sed`

## Alle Zahlen durch `NUMBER` ersetzen

    sed -E 's/[0-9]+/NUMBER/g' datei.txt

## Leerzeichen am Zeilenanfang entfernen

    sed -E 's/^[[:space:]]+//' datei.txt

## Leerzeichen am Zeilenende entfernen

    sed -E 's/[[:space:]]+$//' datei.txt

## Beides zusammen

    sed -E \    -e 's/^[[:space:]]+//' \    -e 's/[[:space:]]+$//' \    datei.txt

## Mehrere Leerzeichen auf eines reduzieren

    sed -E 's/[[:space:]]+/ /g' datei.txt

------------------------------------------------------------------------

# Regex in Python

In Python benutzt du meist das Modul `re`.

    import re

## Suchen

    text = "Meine Nummer ist 4711"  
      
    match = re.search(r"[0-9]+", text)  
      
    if match:  
    print(match.group())

## Alle Treffer

    numbers = re.findall(r"[0-9]+", "12 Äpfel und 5 Birnen")  
      
    print(numbers)

Ergebnis:

    ["12", "5"]

## Ersetzen

    text = "Hallo Maik"  
      
    result = re.sub(r"\s+", " ", text)  
      
    print(result)

## Ganze Zeichenkette prüfen

    postal_code = "45739"  
      
    if re.fullmatch(r"[0-9]{5}", postal_code):  
    print("Gültige Postleitzahl")

`fullmatch()` ist praktisch, weil du nicht extra `^` und `$` schreiben musst.

------------------------------------------------------------------------

# Rohstrings in Python

In Python solltest du Regex meistens mit `r` schreiben:

    r"\d+\.\d+"

statt:

    "\\d+\\.\\d+"

Das `r` bedeutet Raw String. Dadurch verarbeitet Python die Backslashes nicht vorher selbst.

------------------------------------------------------------------------

# Die 12 Muster, die du wirklich im Kopf haben solltest

    ^Text beginnt mit Text  
    Text$ endet mit Text  
    ^Text$ exakt Text  
    . ein beliebiges Zeichen  
    .* beliebig viele Zeichen  
    [0-9] eine Ziffer  
    [0-9]+ mindestens eine Ziffer  
    [^;]+ mindestens ein Zeichen außer ;  
    a|b a oder b  
    (ab)+ Gruppe mindestens einmal  
    [0-9]{5} genau fünf Ziffern  
    ^[[:space:]]*$ leere oder scheinbar leere Zeile

## Ein sehr wichtiger Denkfehler

    .*

bedeutet nicht:

    irgendetwas Bestimmtes

sondern:

    möglicherweise auch gar nichts

Denn:

    .  = ein beliebiges Zeichen*  = nullmal oder öfter

Dagegen bedeutet:

    .+

    mindestens ein beliebiges Zeichen

Für deine Lernreihe würde ich Regex direkt mit realen Daten üben:

    grep  → Treffer findensed   → Treffer verändernawk   → Felder mit Regex auswählenPython re → kontrolliert prüfen und umformenSQLite → meist LIKE, GLOB oder zusätzliche Regex-Funktion

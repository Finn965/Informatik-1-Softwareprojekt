# Informatik-Projekt_1: Tic-Tac-Toe Python Programm

## Kurzbeschreibung

Dieses Programm ist ein **Tic-Tac-Toe-Spiel für das Terminal**, das in Python geschrieben wurde.

## Funktionen

- Zwei Spielmodi:
  - **Spieler gegen KI**
  - **Zwei Spieler (Coop-Modus)**

- Drei Schwierigkeitsstufen für die KI:
  - **Leicht**: zufällige Züge
  - **Mittel**: Mischung aus zufälligen und strategischen Zügen
  - **Schwer**: nutzt den Minimax-Algorithmus für optimale Entscheidungen

## Spielablauf

- Das Spielfeld ist ein 3×3-Gitter.
- Spieler setzen abwechselnd **X** und **O**.
- Nach jedem Zug wird das Spielfeld aktualisiert angezeigt.
- Das Spiel prüft automatisch:
  - Gewinn (Reihe, Spalte oder Diagonale)
  - Unentschieden

## Weitere Features

- Eingaben werden auf Gültigkeit überprüft.
- Der Spielstand wird über mehrere Runden gespeichert.
- Spieler können nach jeder Runde entscheiden, ob sie weiterspielen möchten.

## Python-Version

Version: 3.12.1

## Beispielhafte Nutzung

### Programmeingabe (User-Input)

Willkommen zum Tic-Tac-Toe!

Wähle Modus (ki/coop): ki

Wähle Schwierigkeit (leicht/mittel/schwer): leicht

Spieler 1, wähle ein Feld (0–8): 0


### Beispielausgabe (Konsole)

X | 1 | 2    
3 | 4 | 5    
6 | 7 | 8    

Zug vom Bot:

X | 1 | 2    
3 | O | 5    
6 | 7 | 8    

Spieler 1, wähle ein Feld (0–8): 1

X | X | 2   
3 | O | 5   
6 | 7 | 8   

Zug vom Bot:

X | 1 | 2    
O | O | 5    
6 | 7 | 8    


### Beispiel für Spielende

X | X | X   
O | O | 5   
6 | 7 | 8   

Spieler 1 hat gewonnen!

Aktueller Spielstand:
Spieler 1: 1
Spieler 2: 0

Willst du noch eine Runde spielen? (ja/nein)

nein

Programm beendet


## Hinweis

- Zahlen (0–8) stehen für freie Felder.
- `X` = Spieler 1  
- `O` = Spieler 2 bzw. KI

## Teammitglieder

Quang Schulz, Fabienne Fechter, Felix Rösch, Finn Dahlmanns, Marvin Gorbach 
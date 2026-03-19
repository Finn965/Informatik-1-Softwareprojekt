
## Einzelne Funktions-Flowcharts

### `menue.py` – `hauptmenue()`
```mermaid
flowchart TD
    Start([Start])
    Start --> PrintTitle["Titel und Menü anzeigen"]

    PrintTitle --> ModeLoop{"Ist ein Spielmodus ausgewählt?"}
    ModeLoop -- Nein --> InputMode["Spieler gibt 1 oder 2 ein"]
    InputMode --> ValidateMode{"Ist die Eingabe gültig?"}
    ValidateMode -- Nein --> PrintInvalid["Fehlermeldung anzeigen"]
    PrintInvalid --> ModeLoop
    ValidateMode -- Ja --> ModeChoice{"Co-op oder KI?"}

    ModeChoice -- Ja --> CoOp["Co-op-Modus starten"]
    ModeChoice -- Nein --> KIStart["KI-Modus starten"]

    KIStart --> DiffLoop{"Ist eine Schwierigkeit ausgewählt?"}
    DiffLoop -- Nein --> InputDiff["Spieler gibt 1, 2 oder 3 ein"]
    InputDiff --> ValidateDiff{"Ist die Eingabe gültig?"}
    ValidateDiff -- Nein --> PrintInvalidDiff["Fehlermeldung anzeigen"]
    PrintInvalidDiff --> DiffLoop
    ValidateDiff -- Ja --> ChooseDiff{"Ist die Schwierigkeit 'Leicht'?"}
    ChooseDiff -- Ja --> Easy["Schwierigkeit auf 'Leicht' stellen"]
    ChooseDiff -- Nein --> ChooseDiff2{"Ist die Schwierigkeit 'Mittel'?"}
    ChooseDiff2 -- Ja --> Medium["Schwierigkeit auf 'Mittel' stellen"]
    ChooseDiff2 -- Nein --> Hard["Schwierigkeit auf 'Schwer' stellen"]
```

### `main.py` – `main()`
```mermaid
flowchart TD
    Start([Start])
    Start --> LoopStart["Programm startet"]
    LoopStart --> Menu["Menü anzeigen und Einstellungen holen"]
    Menu --> Init["Spielbrett zurücksetzen & anzeigen"]

    Loop["Spiel läuft"]
    Init --> Loop

    subgraph CoOp
        direction TB
        Loop --> CoOpCheck{"Ist Co-op ausgewählt?"}
        CoOpCheck -- Ja --> CoOpMoves["Spieler 1 und 2 wechseln sich ab"]
    end

    subgraph KI
        direction TB
        Loop --> KICheck{"Ist KI-Modus ausgewählt?"}
        KICheck -- Ja --> PlayerTurn{"Ist Spieler an der Reihe?"}
        PlayerTurn -- Ja --> PlayerMove["Spieler macht Zug"]
        PlayerTurn -- Nein --> BotMove["Computer macht Zug"]
    end

    Loop --> EndCheck{"Ist das Spiel beendet?"}
    EndCheck -- Ja --> Score["Punkte aktualisieren & anzeigen"]
    Score --> Replay{"Möchte man noch eine Runde?"}
    Replay -- ja --> Init
    Replay -- nein --> End["Programm beenden"]

    End --> Stop([Ende])
```

### `logic.py` – `input_gamestep()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Loop["Wiederhole bis gültig"]
    Loop --> Prompt["Spieler wählt ein Feld"]

    Prompt --> IsDigit{"Eingabe ist eine Zahl?"}
    IsDigit -- Nein --> ErrNotDigit["Fehler: Bitte Zahl eingeben"]
    ErrNotDigit --> Loop

    IsDigit -- Ja --> ToInt["Zahl übernehmen"]
    ToInt --> InRange{"Zahl zwischen 0 und 8?"}
    InRange -- Nein --> ErrRange["Fehler: Zahl ungültig"]
    ErrRange --> Loop

    InRange -- Ja --> CalcRC["Feldposition berechnen"]
    CalcRC --> FreeCheck{"Ist das Feld noch frei?"}
    FreeCheck -- Nein --> ErrTaken["Fehler: Feld bereits belegt"]
    ErrTaken --> Loop

    FreeCheck -- Ja --> Return["Feld zurückgeben"]
```

### `logic.py` – `set_move()`
```mermaid
flowchart TD
    Start([Start])
    Start --> ForRow["Jede Zeile prüfen"]
    ForRow --> ForCol["Jede Spalte prüfen"]
    ForCol --> Match{"Ist dies das gewählte Feld?"}
    Match -- Ja --> Set["Feld belegen"]
    Match -- Nein --> Skip
    Set --> Skip
    Skip --> LoopEnd["Alle Felder geprüft"]
    LoopEnd --> Return["Aktualisiertes Spielbrett zurückgeben"]
```

### `logic.py` – `gamestatus()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Win1["Prüfe: hat Spieler 1 gewonnen?"]
    Win1 -- Ja --> Return1["Rückgabe: Spieler 1 gewinnt"]
    Win1 -- Nein --> Win2["Prüfe: hat Spieler 2 gewonnen?"]
    Win2 -- Ja --> Return2["Rückgabe: Spieler 2 gewinnt"]
    Win2 -- Nein --> Return0["Rückgabe: kein Gewinner"]
```

### `logic.py` – `spielstand()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Check1{"Hat Spieler 1 gewonnen?"}
    Check1 -- Ja --> Inc1["Punkt für Spieler 1"]
    Inc1 --> Return1["Punktestand zurückgeben"]
    Check1 -- Nein --> Check2{"Hat Spieler 2 gewonnen?"}
    Check2 -- Ja --> Inc2["Punkt für Spieler 2"]
    Inc2 --> Return2["Punktestand zurückgeben"]
    Check2 -- Nein --> ReturnNone["Punktestand unverändert"]
```

### `logic.py` – `wintest()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Map["Symbole für Spieler setzen"]
    Map --> Rows["Reihen prüfen"]
    Rows --> Cols["Spalten prüfen"]
    Cols --> Diag1["Diagonale 1 prüfen"]
    Diag1 --> Diag2["Diagonale 2 prüfen"]
    Diag2 --> ReturnFalse["Kein Gewinner"]

    subgraph RowCheck
        direction TB
        Rows --> RowLoop["Jede Reihe prüfen"]
        RowLoop --> RowCond{"Sind drei Felder gleich?"}
        RowCond -- Ja --> ReturnTrue["Gewinner gefunden"]
    end

    subgraph ColCheck
        direction TB
        Cols --> ColLoop["Jede Spalte prüfen"]
        ColLoop --> ColCond{"Sind drei Felder gleich?"}
        ColCond -- Ja --> ReturnTrue
    end

    subgraph DiagCheck
        direction TB
        Diag1 --> Diag1Cond{"Sind drei Felder gleich?"}
        Diag1Cond -- Ja --> ReturnTrue
        Diag1Cond -- Nein --> Diag2Cond{"Sind drei Felder gleich?"}
        Diag2Cond -- Ja --> ReturnTrue
    end
```

### `logic.py` – `possible_moves()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Init["Liste möglicher Züge anlegen"]
    Init --> ForI["Jede Zeile prüfen"]
    ForI --> ForJ["Jede Spalte prüfen"]
    ForJ --> Check{"Ist Feld frei?"}
    Check -- Ja --> Add["Feld zur Liste hinzufügen"]
    Add --> Continue
    Check -- Nein --> Continue
    Continue --> EndLoops["Alle Felder geprüft"]
    EndLoops --> Return["Liste möglicher Züge zurückgeben"]
```

### `logic.py` – `simulation_easy()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Moves["Freie Felder ermitteln"]
    Moves --> HasMoves{"Gibt es freie Felder?"}
    HasMoves -- Ja --> Choose["Zufälliges Feld wählen"]
    Choose --> Return["Gewählten Zug zurückgeben"]
    HasMoves -- Nein --> ReturnNone["Kein Zug möglich"]
```

### `logic.py` – `simulation_medium()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Rand["Zufall entscheiden lassen"]
    Rand --> Branch{"Zufall entscheidet?"}
    Branch -- Ja --> Easy["Einfachen Zug wählen"]
    Branch -- Nein --> Hard["Besseren Zug wählen"]
```

### `logic.py` – `simulation_difficult()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Moves["Freie Felder ermitteln"]
    Moves --> Init["Besten Zug initialisieren"]
    Init --> Symbol["Symbol des Computers setzen"]
    Symbol --> Loop["Für jedes freie Feld"]
    Loop --> Copy["Spielfeld kopieren"]
    Copy --> Put["Zug auf Kopie setzen"]
    Put --> Eval["Zug bewerten"]
    Eval --> Compare{"Besser als bisher?"}
    Compare -- Ja --> Update["Besten Zug merken"]
    Compare --> Next["Weiter mit nächstem Feld"]
    Next --> Loop
    Loop --> Return["Besten Zug zurückgeben"]
```

### `logic.py` – `minmax()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Moves["Mögliche Züge ermitteln"]
    Moves --> WinBot["Prüfen: gewinnt der Computer?" ]
    WinBot --> WinPlayer["Prüfen: gewinnt der Spieler?"]
    WinPlayer --> CheckWin{"Hat jemand gewonnen?"}
    CheckWin -- won_bot --> ReturnLose["Bewertung: Verlust"]
    CheckWin -- won_player --> ReturnWin["Bewertung: Sieg"]
    CheckWin -- none --> Tie{"Unentschieden?"}
    Tie -- Ja --> ReturnTie["Bewertung: unentschieden"]
    Tie -- Nein --> MaxCheck{"Maximiere oder minimiere?"}

    subgraph MaxBranch
        direction TB
        MaxCheck -- Ja --> MaxInit["Maximieren initialisieren"]
        MaxInit --> MaxLoop["Jeden möglichen Zug durchgehen"]
        MaxLoop --> Apply["Zug anwenden"]
        Apply --> Recurse["Rekursiv bewerten (Minimieren)"]
        Recurse --> UpdateMax["Beste Bewertung merken"]
        UpdateMax --> Undo["Zug rückgängig machen"]
        Undo --> MaxLoop
        MaxLoop --> ReturnMax["Beste Bewertung zurückgeben"]
    end

    subgraph MinBranch
        direction TB
        MaxCheck -- Nein --> MinInit["Minimieren initialisieren"]
        MinInit --> MinLoop["Jeden möglichen Zug durchgehen"]
        MinLoop --> Apply2["Zug des Gegners anwenden"]
        Apply2 --> Recurse2["Rekursiv bewerten (Maximieren)"]
        Recurse2 --> UpdateMin["Schlechteste Bewertung merken"]
        UpdateMin --> Undo2["Zug rückgängig machen"]
        Undo2 --> MinLoop
        MinLoop --> ReturnMin["Schlechteste Bewertung zurückgeben"]
    end
```

### `logic.py` – `output()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Init["Farben und Position initialisieren"]
    Init --> RowLoop["Jede Zeile ausgeben"]
    RowLoop --> CellLoop["Jede Zelle ausgeben"]
    CellLoop --> CheckX{"Ist das Feld X?"}
    CheckX -- Ja --> PrintX["X in Farbe ausgeben"]
    PrintX --> NextCell
    CheckX -- Nein --> CheckO{"Ist das Feld O?"}
    CheckO -- Ja --> PrintO["O in Farbe ausgeben"]
    PrintO --> NextCell
    CheckO -- Nein --> PrintEmpty["Leerfeld ausgeben"]
    PrintEmpty --> NextCell
    NextCell --> ContinueCells
    ContinueCells --> EndRows["Alle Felder ausgegeben"]

    EndRows --> Win1{"Hat Spieler 1 gewonnen?"}
    Win1 -- Ja --> PrintWin1["Gewinnmeldung für Spieler 1"]
    Win1 -- Nein --> Win2{"Hat Spieler 2 gewonnen?"}
    Win2 -- Ja --> PrintWin2["Gewinnmeldung für Spieler 2"]
```
```

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

    A([Start]) --> B[Variablen initialisieren]

    B --> C{Programm läuft?}

    C -->|ja| D["hauptmenue()"<br/>→ Modus, Schwierigkeit]
    D --> E[BORDLIST kopieren]
    E --> F["output(bordlist)"]
    F --> G[Spiel starten]

    G --> H{Spiel aktiv?}

    %% ================= KI MODUS =================
    H -->|ja| I{Modus = KI?}

    I -->|ja| J["gamestatus(bordlist)"]
    J -->|= 0| K{Player1_turn?}

    K -->|ja| L["wintest(bordlist,player2)"]

    L -->|False| M["possible_moves(bordlist)"]

    M -->|Züge vorhanden| N["input_gamestep(bordlist,1)"]
    N --> O["set_move(X, move)"]
    O --> P["output(bordlist)"]
    P --> Q[Player1_turn = False]
    Q --> H

    M -->|keine Züge| R[Unentschieden]
    R --> S[unentschieden = True]
    S --> H

    K -->|nein| T[Bot-Zug]
    T --> U{Schwierigkeit}

    U -->|leicht| V["simulation_easy(bordlist)"]
    U -->|mittel| W["simulation_medium(bordlist,player2)"]
    U -->|schwer| X["simulation_difficult(bordlist,player2)"]

    V --> Y["set_move(O, move)"]
    W --> Y
    X --> Y

    Y --> Z["output(bordlist)"]
    Z --> ZA[Player1_turn = True]
    ZA --> H

    %% ================= COOP MODUS =================
    I -->|"nein (Coop)"| ZB["gamestatus(bordlist)"]

    ZB -->|= 0| ZC["possible_moves(bordlist)"]

    ZC -->|Züge vorhanden| ZD{Player1_turn?}

    ZD -->|ja| ZE["input_gamestep(bordlist,1)"]
    ZE --> ZF["set_move(X, move)"]
    ZF --> ZG["output(bordlist)"]
    ZG --> ZH[Player1_turn = False]
    ZH --> H

    ZD -->|nein| ZI["input_gamestep(bordlist,2)"]
    ZI --> ZJ["set_move(O, move)"]
    ZJ --> ZK["output(bordlist)"]
    ZK --> ZL[Player1_turn = True]
    ZL --> H

    ZC -->|keine Züge| ZM[Unentschieden]
    ZM --> ZN[unentschieden = True]
    ZN --> H

    %% ================= SPIELENDE =================
    H -->|nein| AA[Spielende prüfen]

    AA --> AB{gamestatus != 0<br/>oder unentschieden?}

    AB -->|ja| AC{Ergebnis}

    AC -->|Spieler 1| AD["spielstand(1, Spieler1)"]
    AC -->|Spieler 2| AE["spielstand(2, Spieler2)"]
    AC -->|Unentschieden| AF[Spieler1 +=1<br/>Spieler2 +=1]

    AD --> AG[Spielstand anzeigen]
    AE --> AG
    AF --> AG

    AG --> AH{Noch eine Runde?}

    AH -->|ja| C
    AH -->|nein| AI([Programm beendet])

    AH -->|ungültig| AJ[Fehlermeldung]
    AJ --> AH

    %% Direkter Abbruch
    C -->|nein| AI
```

### `logic.py` – `input_gamestep()`
```mermaid
flowchart TD

    A([Start input_gamestep]) --> B[input Eingabe]
    B --> C{Ist Eingabe eine Zahl?}

    C -->|nein| D[print Fehler]
    D --> B

    C -->|ja| E[move in Zahl umwandeln]

    E --> F{0 bis 8?}

    F -->|nein| G[print Fehler]
    G --> B

    F -->|ja| H[row berechnen]
    H --> I[col berechnen]

    I --> J{Feld frei?}

    J -->|nein| K[print Feld belegt]
    K --> B

    J -->|ja| L[return move]
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


    A(["Start wintest()"]) --> B[symbol Dictionary]
    B --> C[player_symbol bestimmen]

    C --> D{Zeilen prüfen}

    D --> E[reihe 0]
    E --> F{3 gleiche in Reihe?}
    F -->|ja| G[return True]

    F -->|nein| H[reihe 1]
    H --> I{3 gleiche in Reihe?}
    I -->|ja| G
    I -->|nein| J[reihe 2]
    J --> K{3 gleiche in Reihe?}
    K -->|ja| G
    K -->|nein| L[weiter]

    L --> M{Spalten prüfen}

    M --> N[spalte 0]
    N --> O{3 gleiche in Spalte?}
    O -->|ja| G
    O -->|nein| P[spalte 1]
    P --> Q{3 gleiche in Spalte?}
    Q -->|ja| G
    Q -->|nein| R[spalte 2]
    R --> S{3 gleiche in Spalte?}
    S -->|ja| G
    S -->|nein| T[weiter]

    T --> U{Diagonalen prüfen}

    U --> V{Diagonal links oben?}
    V -->|ja| G

    V -->|nein| W{Diagonal rechts oben?}
    W -->|ja| G

    W -->|nein| X[return False]
```

### `logic.py` – `possible_moves()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Init["moves = []"]
    Init --> ForI["for i in range(3)"]
    ForI --> ForJ["for j in range(3)"]
    ForJ --> Check{"board[i][j] nicht X/O?"}
    Check -- Ja --> Add["moves.append((i,j))"]
    Add --> Continue
    Check -- Nein --> Continue
    Continue --> EndLoops["Ende der Schleifen"]
    EndLoops --> Return["return moves"]
```

### `logic.py` – `simulation_easy()`
```mermaid
flowchart TD

    A([Start simulation_easy]) --> B["possible_moves()"]

    B --> C{Züge vorhanden?}

    C -->|nein| D[return None]

    C -->|ja| E["random.choice()"]
    E --> F[random_move bestimmen]

    F --> G[Zug aus bordlist lesen]

    G --> H[return Zug]
```

### `logic.py` – `simulation_medium()`
```mermaid
flowchart TD

    A([Start simulation_medium]) --> B["random.random()"]

    B --> C{Zufallswert < 0.3?}

    C -->|ja| D["simulation_easy()"]
    D --> E[return zufälliger Zug]

    C -->|nein| F["simulation_difficult()"]
    F --> G[return bester Zug]
```

### `logic.py` – `simulation_difficult()`
```mermaid
flowchart TD

    A(["Start simulation_difficult()"]) --> B["possible_moves()"]
    B --> C{Züge vorhanden?}

    C -->|ja| D[best_result = -2]
    C -->|nein| Z([Ende])

    D --> E{bot_playernumber?}

    E -->|player1| F[bot_playersymbol = X]
    E -->|player2| G[bot_playersymbol = O]

    F --> H[Schleife über alle Züge]
    G --> H

    
    I --> J[Zug setzen]

    J --> K["minmax() aufrufen"]

    K --> L{minimax_result > best_result?}

    L -->|ja| M[best_result aktualisieren]
    M --> N[best_move speichern]
    L -->|nein| N

    N --> H

    H --> O[Alle Züge geprüft?]
    O -->|nein| I["copy.deepcopy()"]
    O -->|ja| P[best_move zurückgeben]

    P --> Z([Ende])
```

### `logic.py` – `minmax()`
```mermaid
flowchart TD

    A([Start minmax]) --> B["possible_moves()"]
    B --> C[wintest Bot]
    C --> D[wintest Gegner]

    D --> E{Endzustand?}

    E -->|Bot gewinnt| F[return 1]
    E -->|Gegner gewinnt| G[return -1]
    E -->|Unentschieden| H[return 0]

    E -->|weiter| I{maximizingPlayer?}

    %% ================= MAX =================
    I -->|ja| J[maxEval = sehr klein]

    J --> K[Für jeden Zug]

    K --> L[Zug setzen]
    L --> M["minmax() False"]
    M --> N[maxEval aktualisieren]
    N --> O[Zug rückgängig machen]

    O --> K

    K --> P{weitere Züge?}
    P -->|ja| K
    P -->|nein| Q[return maxEval]

    %% ================= MIN =================
    I -->|nein| R[minEval = sehr groß]

    R --> S[Für jeden Zug]

    S --> T[Zug setzen]
    T --> U["minmax() True"]
    U --> V[minEval aktualisieren]
    V --> W[Zug rückgängig machen]

    W --> S

    S --> X{weitere Züge?}
    X -->|ja| S
    X -->|nein| Y[return minEval]
```

### `logic.py` – `output()`
```mermaid
flowchart TD

    A(["Start output()"]) --> B[Variablen setzen<br/>Farben + rowcounter]

    B --> C[Äußere Schleife über boardlist]

    C --> Z{Alle Zeilen fertig?}

    Z -->|ja| AA[wintest player1]

    AA -->|true| AB["print(Spieler 1 hat gewonnen)"]

    AA -->|false| AC[wintest player2]

    AC -->|true| AD["print(Spieler 2 hat gewonnen)"]

    AC -->|false| AE([Ende])

    AB --> AE
    AD --> AE

    C --> D[Innere Schleife über Zeile]

    D --> E{Wert = X?}

    E -->|ja| F[print rot]
    F --> G{rowcounter < 2?}

    G -->|ja| H["print (X |)"]
    H --> I[rowcounter +1]

    G -->|nein| J["print(X)"]
    J --> K[rowcounter = 0]

    E -->|nein| L{Wert = O?}

    L -->|ja| M[print grün]
    M --> N{rowcounter < 2?}

    N -->|ja| O["print(O |)"]
    O --> P[rowcounter +1]

    N -->|nein| Q["print(O)"]
    Q --> R[rowcounter = 0]

    L -->|nein| S[print Standard]
    S --> T{rowcounter < 2?}

    T -->|ja| U["print(Wert |)"]
    U --> V[rowcounter +1]

    T -->|nein| W["print(Wert)"]
    W --> X[rowcounter = 0]

    I --> D
    K --> D
    P --> D
    R --> D
    V --> D
    X --> D

    D --> Y{Zeile fertig?}
    Y -->|nein| D
    Y -->|ja| C
```
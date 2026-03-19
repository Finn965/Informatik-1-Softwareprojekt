
## Einzelne Funktions-Flowcharts

### `menue.py` – `hauptmenue()`
```mermaid
flowchart TD
    Start([Start])
    Start --> PrintTitle["Titel & Menü-Rahmen ausgeben"]

    ModeLoop{"modus in [1,2]?"}
    ModeLoop -- Nein --> InputMode["input('Eingabe (1 oder 2): ')"]
    InputMode --> ValidateMode{modus gültig?}
    ValidateMode -- Nein --> PrintInvalid["Fehler: ungültige Eingabe"]
    PrintInvalid --> ModeLoop
    ValidateMode -- Ja --> ModeChoice{"modus == 1?"}

    ModeChoice -- Ja --> CoOp["return 'coop', None"]
    ModeChoice -- Nein --> KIStart["Schwierigkeit wählen"]

    KIStart --> DiffLoop{"schwierigkeit in [1,2,3]?"}
    DiffLoop -- Nein --> InputDiff["input('Eingabe (1, 2 oder 3): ')"]
    InputDiff --> ValidateDiff{gültig?}
    ValidateDiff -- Nein --> PrintInvalidDiff["Fehler: ungültige Eingabe"]
    PrintInvalidDiff --> DiffLoop
    ValidateDiff -- Ja --> ChooseDiff{"schwierigkeit == 1?"}
    ChooseDiff -- Ja --> Easy["return 'ki','leicht'"]
    ChooseDiff -- Nein --> ChooseDiff2{"schwierigkeit == 2?"}
    ChooseDiff2 -- Ja --> Medium["return 'ki','mittel'"]
    ChooseDiff2 -- Nein --> Hard["return 'ki','schwer'"]
```

### `main.py` – `main()`
```mermaid
flowchart TD
    Start([Start])
    Start --> LoopStart["programmläuft = True"]
    LoopStart --> Menu["modus, schwierigkeit = hauptmenue()"]
    Menu --> Init["bordlist zurücksetzen + output(bordlist)"]

    Loop["while aktuelles_Spiel:"]
    Init --> Loop

    subgraph CoOp
        direction TB
        Loop --> CoOpCheck{"modus == coop und gamestatus == 0?"}
        CoOpCheck -- Ja --> CoOpMoves["Wechselnde Spielerzüge (input_gamestep + set_move + output)"]
    end

    subgraph KI
        direction TB
        Loop --> KICheck{"modus == ki und gamestatus == 0?"}
        KICheck -- Ja --> PlayerTurn{Player1_turn?}
        PlayerTurn -- Ja --> PlayerMove["input_gamestep + set_move('X') + output"]
        PlayerTurn -- Nein --> BotMove["KI-Zug (simulation_*(...) + set_move('O') + output)"]
    end

    Loop --> EndCheck{gamestatus != 0 oder unentschieden?}
    EndCheck -- Ja --> Score["spieler1/2 aktualisieren + ausgeben"]
    Score --> Replay{nochmal?}
    Replay -- ja --> Init
    Replay -- nein --> End["programmläuft=False"]

    End --> Stop([Ende])
```

### `logic.py` – `input_gamestep()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Loop["while True"]
    Loop --> Prompt["input('Spieler ..., wähle Feld')"]

    Prompt --> IsDigit{"move.isdigit()?"}
    IsDigit -- Nein --> ErrNotDigit["Fehler ausgeben"]
    ErrNotDigit --> Loop

    IsDigit -- Ja --> ToInt["move = int(move)"]
    ToInt --> InRange{0 <= move <= 8?}
    InRange -- Nein --> ErrRange["Fehler ausgeben"]
    ErrRange --> Loop

    InRange -- Ja --> CalcRC["row = move // 3, col = move % 3"]
    CalcRC --> FreeCheck{feld frei?}
    FreeCheck -- Nein --> ErrTaken["Fehler ausgeben"]
    ErrTaken --> Loop

    FreeCheck -- Ja --> Return["return move"]
```

### `logic.py` – `set_move()`
```mermaid
flowchart TD
    Start([Start])
    Start --> ForRow["for reihe in range(3)"]
    ForRow --> ForCol["for spalte in range(3)"]
    ForCol --> Match{"bordlist[reihe][spalte] == move?"}
    Match -- Ja --> Set["bordlist[reihe][spalte] = player"]
    Match -- Nein --> Skip
    Set --> Skip
    Skip --> LoopEnd["Ende der Schleifen"]
    LoopEnd --> Return["return bordlist"]
```

### `logic.py` – `gamestatus()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Win1["wintest(bordlist,'player1')"]
    Win1 -- Ja --> Return1["return 1"]
    Win1 -- Nein --> Win2["wintest(bordlist,'player2')"]
    Win2 -- Ja --> Return2["return 2"]
    Win2 -- Nein --> Return0["return 0"]
```

### `logic.py` – `spielstand()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Check1{"winner == 1?"}
    Check1 -- Ja --> Inc1["score += 1"]
    Inc1 --> Return1["return score"]
    Check1 -- Nein --> Check2{"winner == 2?"}
    Check2 -- Ja --> Inc2["score += 1"]
    Inc2 --> Return2["return score"]
    Check2 -- Nein --> ReturnNone["return None"]
```

### `logic.py` – `wintest()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Map["Symbol = {'player1':'X','player2':'O'}"]
    Map --> Rows["Zeilen prüfen"]
    Rows --> Cols["Spalten prüfen"]
    Cols --> Diag1["Diagonal 1 prüfen"]
    Diag1 --> Diag2["Diagonal 2 prüfen"]
    Diag2 --> ReturnFalse["return False"]

    subgraph RowCheck
        direction TB
        Rows --> RowLoop["for reihe in range(3)"]
        RowLoop --> RowCond{alle 3 gleich?}
        RowCond -- Ja --> ReturnTrue["return True"]
    end

    subgraph ColCheck
        direction TB
        Cols --> ColLoop["for spalte in range(3)"]
        ColLoop --> ColCond{alle 3 gleich?}
        ColCond -- Ja --> ReturnTrue
    end

    subgraph DiagCheck
        direction TB
        Diag1 --> Diag1Cond{alle 3 gleich?}
        Diag1Cond -- Ja --> ReturnTrue
        Diag1Cond -- Nein --> Diag2Cond{alle 3 gleich?}
        Diag2Cond -- Ja --> ReturnTrue
    end
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
    Start([Start])
    Start --> Moves["move = possible_moves(bordlist)"]
    Moves --> HasMoves{"move != []?"}
    HasMoves -- Ja --> Choose["random.choice(move)"]
    Choose --> Return["return bordlist[random_move[0]][random_move[1]]"]
    HasMoves -- Nein --> ReturnNone["return None"]
```

### `logic.py` – `simulation_medium()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Rand["choice = random.random()"]
    Rand --> Branch{choice < 0.5?}
    Branch -- Ja --> Easy["return simulation_easy(bordlist)"]
    Branch -- Nein --> Hard["return simulation_difficult(bordlist, playernumber)"]
```

### `logic.py` – `simulation_difficult()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Moves["possiblemoves = possible_moves(bordlist)"]
    Moves --> Init["best_result=-2, best_move=None"]
    Init --> Symbol["bot_playersymbol bestimmen"]
    Symbol --> Loop["für jedes x in possiblemoves"]
    Loop --> Copy["simulation_bord = deepcopy(bordlist)"]
    Copy --> Put["simulation_bord[x] = bot_playersymbol"]
    Put --> Eval["minimax_result = minmax(...)"]
    Eval --> Compare{> best_result?}
    Compare -- Ja --> Update["best_result=..., best_move=... "]
    Compare --> Next["nächster Zug"]
    Next --> Loop
    Loop --> Return["return best_move"]
```

### `logic.py` – `minmax()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Moves["possible_move = possible_moves(bordlist)"]
    Moves --> WinBot["won_bot = wintest(...)"]
    WinBot --> WinPlayer["won_player = wintest(...)"]
    WinPlayer --> CheckWin{won_bot oder won_player?}
    CheckWin -- won_bot --> ReturnLose["return 1"]
    CheckWin -- won_player --> ReturnWin["return -1"]
    CheckWin -- none --> Tie{"len(possible_move)==0?"}
    Tie -- Ja --> ReturnTie["return 0"]
    Tie -- Nein --> MaxCheck{maximizingPlayer?}

    subgraph MaxBranch
        direction TB
        MaxCheck -- Ja --> MaxInit["maxEval=-100000"]
        MaxInit --> MaxLoop["für jeden child in possible_move"]
        MaxLoop --> Apply["bordlist[child]=symbol[bot] "]
        Apply --> Recurse["eval=minmax(..., False)"]
        Recurse --> UpdateMax["maxEval=max(maxEval, eval)"]
        UpdateMax --> Undo["bordlist[child]=original"]
        Undo --> MaxLoop
        MaxLoop --> ReturnMax["return maxEval"]
    end

    subgraph MinBranch
        direction TB
        MaxCheck -- Nein --> MinInit["minEval=+100000"]
        MinInit --> MinLoop["für jeden child in possible_move"]
        MinLoop --> Apply2["bordlist[child]=symbol(opponent)"]
        Apply2 --> Recurse2["eval=minmax(..., True)"]
        Recurse2 --> UpdateMin["minEval=min(minEval, eval)"]
        UpdateMin --> Undo2["bordlist[child]=original"]
        Undo2 --> MinLoop
        MinLoop --> ReturnMin["return minEval"]
    end
```

### `logic.py` – `output()`
```mermaid
flowchart TD
    Start([Start])
    Start --> Init["Farben & rowcounter initialisieren"]
    Init --> RowLoop["für i in boardlist"]
    RowLoop --> CellLoop["für y in i"]
    CellLoop --> CheckX{"y == X?"}
    CheckX -- Ja --> PrintX["rot ausgeben + Separator"]
    PrintX --> NextCell
    CheckX -- Nein --> CheckO{"y == O?"}
    CheckO -- Ja --> PrintO["grün ausgeben + Separator"]
    PrintO --> NextCell
    CheckO -- Nein --> PrintEmpty["Standardfarbe ausgeben + Separator"]
    PrintEmpty --> NextCell
    NextCell --> ContinueCells
    ContinueCells --> EndRows["Ende aller Zellen"]

    EndRows --> Win1{"wintest(...,player1)?"}
    Win1 -- Ja --> PrintWin1["'Spieler 1 hat gewonnen!' ausgeben"]
    Win1 -- Nein --> Win2{"wintest(...,player2)?"}
    Win2 -- Ja --> PrintWin2["'Spieler 2 hat gewonnen!' ausgeben"]
```
```

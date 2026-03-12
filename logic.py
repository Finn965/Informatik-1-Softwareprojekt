
"""
    Fragt den Spieler nach einem Zug (0-8),
    prüft ob die Eingabe gültig ist und das Feld frei ist.
    boardlist: Liste mit 9 Elementen (['X', 'O' oder ' '])
    player: aktueller Spieler 'X' oder 'O'
"""

def input_gamestep(bordlist, player):

    while True:
        move = input(f"Spieler {player}, wähle ein Feld (0–8): ")

        # Prüfen, ob Eingabe eine Zahl ist
        if not move.isdigit():
            print("Error! Ungültige Eingabe! Bitte eine Zahl zwischen 0 und 8 eingeben.")
            continue
        move = int(move)

         # Prüfen, ob Zahl im gültigen Bereich liegt
        if move < 0 or move > 8:
            print("Error! Ungültige Position! Nur Zahlen zwischen 0 und 8 sind erlaubt.")
            continue

        row = move // 3
        col = move % 3

        # Prüfen, ob das Feld frei ist
        if boardlist[row][col] != move:
            print("Error! Dieses Feld ist bereits belegt! Wähle ein anderes Feld.")
            continue
    
    return move

    """
    Fragt den Spielmodus ab:
    1 = gegen Freund
    2 = gegen KI

    Wenn KI gewählt wird, wird zusätzlich die Schwierigkeit abgefragt:
    1 = leicht
    2 = mittel
    3 = schwer

    Rückgabe:
    (mode, difficulty)
    mode: "friend" oder "ai"
    difficulty: None, "easy", "medium", "hard"
    """
def choose_gamemode():
    while True:
        mode = input("Wähle den Spielmodus:\n1 - Gegen Freund\n2 - Gegen KI\nEingabe: ")

        if mode == "1":
            return "friend", None

        elif mode == "2":

             while True:
                difficulty = input(
                    "Wähle die Schwierigkeit:\n"
                    "1 - Leicht\n"
                    "2 - Mittel\n"
                    "3 - Schwer\n"
                    "Eingabe: "
                )
                if difficulty == "1":
                    return "ai", "easy"

                elif difficulty == "2":
                    return "ai", "medium"

                elif difficulty == "3":
                    return "ai", "hard"

                else:
                    print("Error! Bitte 1, 2 oder 3 eingeben.")

        else:
            print("Error! Bitte 1 oder 2 eingeben.")


def wintest(bordlist, player):
    return

def possible_moves(bordlist):
    return


def minmax(bordlist:list, bot_playernumber:str): 
    "Minimax Algorithmus"

    if bot_playernumber == "1": #bot spielt "X"
        maximizingPlayer = True
    else:                       #bot spielt "O"
        maximizingPlayer = False

    possible_move = possible_moves(bordlist) #brauche hier noch funktion für mögliche züge, bestenfalls in koordinatenform 


    won_bot =  wintest(bordlist,bot_playernumber) #brauche hier noch funktion gewonnen oder nicht
    won_player = wintest(bordlist,"1" if bot_playernumber==2 else "2") #brauche hier noch funktion gewonnen oder nicht
    if won_bot == True: #verloren
        return 1
    elif won_player == True:#gewonnen
        return -1
    elif len(possible_move) == 0: #unentschieden muss schauen ob möglich mit funktion (possible_moves)
        return 0 
    
    if maximizingPlayer: #wollen das best mögliche ergebnis
        maxEval = -100000
        for child in possible_move:
            bordlist[child[0]][child[1]] = "X" #spielt simulierten zug / kann sein das mit funktion(possible_moves) nicht mehr möglich
            eval = minmax(bordlist, "2") 
            maxEval = max(maxEval, eval) #maximaler wert
        return maxEval
    else: # wollen das schlecht möglichste ergebnis
        minEval = +100000
        for child in possible_move:
            bordlist[child[0]][child[1]] = "O"
            eval = minmax(bordlist, "1")
            minEval = min(minEval, eval) # minimaler wert
        return minEval


if __name__ == "__main__": #bordliste zum testen im logic.py file
    bordliste = [["X","O","X"],["X","O",5],[6,7,"O"]]
    
def output(boardlist):

#definieren der Konstanten der Farben "standard", "rot" und "grün" und der Variable für die Zeile
    ENDC        = "\033[0m"        
    RED         = "\033[91m"
    GREEN       = "\033[92m"
    rowcounter  = 0

    for i in boardlist: #for-schleife für die Ausgabe des aktuellen Spielboardes
        for y in i:
            if y == "X": #Ausgabe in rot, falls Listenstelle ein "X" enthält
                if rowcounter < 2: #Ausgabe mit "|", wenn nicht an rechtester Stelle auf dem Board
                    print(f'{RED}{y}{ENDC}', end="")
                    print(" | ", end="")
                    rowcounter += 1
                else: #Ausgabe ohne "|", wenn nicht an rechtester Stelle auf dem Board
                    print(f'{RED}{y}{ENDC}')
                    rowcounter = 0

            elif y == "O": #Ausgabe in grün, falls Listenstelle ein "O" enthält
                if rowcounter < 2:#Ausgabe mit "|", wenn nicht an rechtester Stelle auf dem Board
                    print(f'{GREEN}{y}{ENDC}', end="")
                    print(" | ", end="")
                    rowcounter += 1
                else: #Ausgabe ohne "|", wenn nicht an rechtester Stelle auf dem Board
                    print(f'{GREEN}{y}{ENDC}')
                    rowcounter = 0

            else: #Ausgabe in Standardfarbe, falls Listenstelle weder "X" noch "O" enthält
                if rowcounter < 2: #Ausgabe mit "|", wenn nicht an rechtester Stelle auf dem Board
                    print(f'{y}', end="")
                    print(" | ", end="")
                    rowcounter += 1
                else: #Ausgabe ohne "|", wenn nicht an rechtester Stelle auf dem Board
                    print(f'{y}')
                    rowcounter = 0

    if wintest(boardlist, "player1") == True: #Outputnachricht, wenn Spieler 1 gewonnen hat
          print(boardlist)
          print("Spieler 1 hat gewonnen!")

    elif wintest(boardlist, "player2") == True: #Outputnachricht, wenn Spieler 2 gewonnen hat
          print(boardlist)
          print("Spieler 2 hat gewonnen!")

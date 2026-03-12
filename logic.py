
def wintest(bordlist, player): # Funktion, die überprüft, ob ein Spieler gewonnen hat
    symbol = {"player1" : "X","player2" : "O"}  # Dictionary mit der Zuordnung von Symbolen zu den Spielern
    player_symbol = symbol[player]
    for reihe in range (3):
        if bordlist [reihe][0] == player_symbol and bordlist [reihe][1] == player_symbol and bordlist [reihe][2] ==player_symbol:  # Prüfen, ob es drei gleiche in einer Zeile sind
            return True
    for spalte in range (3):
        if bordlist [spalte][0] == player_symbol and bordlist [spalte][1] == player_symbol and bordlist [spalte][2] == player_symbol: # Prüfen, ob es drei gleiche in einer Spalte sind
            return True
    if bordlist [0][0] == player_symbol and  bordlist [1][1] == player_symbol and bordlist [2][2] == player_symbol:       # Prüfe die Diagonale von links oben nach rechts unten
            return True
    if bordlist [0][2] == player_symbol and  bordlist [1][1] == player_symbol and bordlist [2][0] == player_symbol:          # Prüfe die Dagonale von rechts oben nach links unten
            return True
    return False  


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

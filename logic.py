import copy #wird für die Simulationen benötigt, damit das Originalbord nicht verändert wird

def wintest(bordlist, player): # Funktion, die überprüft, ob ein Spieler gewonnen hat
    symbol = {"player1" : "X","player2" : "O"}  # Dictionary mit der Zuordnung von Symbolen zu den Spielern
    player_symbol = symbol[player]
    for reihe in range (3):
        if bordlist [reihe][0] == player_symbol and bordlist [reihe][1] == player_symbol and bordlist [reihe][2] ==player_symbol:  # Prüfen, ob es drei gleiche in einer Zeile sind
            return True
    for spalte in range (3):
        if bordlist [0][spalte] == player_symbol and bordlist [1][spalte] == player_symbol and bordlist [2][spalte] == player_symbol: # Prüfen, ob es drei gleiche in einer Spalte sind
            return True
    if bordlist [0][0] == player_symbol and  bordlist [1][1] == player_symbol and bordlist [2][2] == player_symbol:       # Prüfe die Diagonale von links oben nach rechts unten
            return True
    if bordlist [0][2] == player_symbol and  bordlist [1][1] == player_symbol and bordlist [2][0] == player_symbol:          # Prüfe die Dagonale von rechts oben nach links unten
            return True
    return False  





def possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                moves.append((i, j))
    return moves



def simulation_easy():
    pass
def simulation_medium():
    pass

def simulation_difficult(bordlist:list, bot_playernumber:str): #bot_playernumber = player1 or player2
    "Gibt den best möglichen zug für den aktuellen Spielstand aus"
    possiblemoves = possible_moves(bordlist)
    best_result = -2 # kleiner wert zum ersten mal vergleichen 
    if bot_playernumber=="player1": 
        bot_playersymbol = "X"
    else:
        bot_playersymbol = "O"
    
    for x in possiblemoves: #geht alle möglichen züge durch 
        
        simulation_bord = copy.deepcopy(bordlist) #kopiert das bord damit es nicht mit dem orginalen bord verlinkt ist  

        simulation_bord[x[0]][x[1]] = bot_playersymbol #bord für alle möglichen züge
        minimax_result = minmax(simulation_bord, bot_playernumber[-1:], True)

        if minimax_result > best_result: #gibt uns den besten move raus
            best_result = minimax_result
            best_move = bordlist[x[0]][x[1]]
        print("best_result:", best_result)
        print("best_move:", best_move)
        
    return best_move

def minmax(bordlist:list, bot_playernumber:str, maximizingPlayer):
    "Minimax Algorithmus"
    symbol = {"1":"X", "2":"O"}

    possible_move = possible_moves(bordlist) #brauche hier noch funktion für mögliche züge, bestenfalls in koordinatenform 

    #wintest
    won_bot =  wintest(bordlist,"player"+bot_playernumber) 
    won_player = wintest(bordlist,"player"+("1" if bot_playernumber=="2" else "2"))
    if won_bot == True: #verloren
        return 1
    elif won_player == True:#gewonnen
        return -1
    elif len(possible_move) == 0: #unentschieden muss schauen ob möglich mit funktion (possible_moves)
        return 0 
    

    if maximizingPlayer: #wollen das best mögliche ergebnis
        maxEval = -100000
        for child in possible_move:
            bordlist[child[0]][child[1]] = symbol["1" if bot_playernumber=="2" else "2"] #spielt simulierten zug / absichtlich den mensch spielen lassen, da wird den menschen maximieren wollen 
            eval = minmax(bordlist, bot_playernumber, False) 
            print("eval max",eval)
            maxEval = max(maxEval, eval) #maximaler wert
            bordlist[child[0]][child[1]] = child[0]*3 + child[1] + 1 #macht den zug rückgängig
        return maxEval
    else: # wollen das schlecht möglichste ergebnis
        minEval = +100000
        for child in possible_move:
            bordlist[child[0]][child[1]] = symbol[bot_playernumber] # hier eingeben was minimiert werden soll 
            eval = minmax(bordlist, ("1" if bot_playernumber=="2" else "2") , True)
            print("eval min",eval)
            minEval = min(minEval, eval) # minimaler wert
            bordlist[child[0]][child[1]] = child[0]*3 + child[1] + 1 #macht den zug rückgängig
        return minEval


if __name__ == "__main__": #bordliste zum testen im logic.py file
    bordliste = [["X", 1 , "O" ],
                 ["O","O", 5 ],
                 ["X",7,"X"]]
    print(simulation_difficult(bordliste, "player1"))
    
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

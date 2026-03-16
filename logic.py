import copy #wird für die simulation_difficult benötigt, damit das Originalbord nicht verändert wird
import random #wird für die simulation_easy benötigt, damit ein zufälliger Zug zurückgegeben werden kann

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

def simulation_easy(bordlist,playernumber): # Funktion, die einen zufälligen Zug zurückgibt
    if playernumber == "player1":  # Legt die Spielersymbole fest
        player_symbol = "X"
    else:        
        player_symbol = "O"
    move = possible_moves(bordlist)            
    if move:                                #Prüfung, ob es noch mögliche Züge gibt
         move_set= random.choice(move)      #wählt zufällig einen der möglichen Züge aus.
         bordlist[move_set[0]][move_set[1]] = player_symbol #setzt den Zug auf dem Bord
         return bordlist
    return None

def simulation_medium(): # Funnktion, die zu 50% einen zufälligen Zug zurückgibt und zu 50% den besten Zug zurückgibt
    
    pass

def simulation_difficult(bordlist:list, bot_playernumber:str): #bot_playernumber = player1 or player2
    """Gibt einen der  best möglichen Züge für das aktuelle Bord aus. 
    
    Die Funktion probiert für jedes freie Feld einen Zug aus und wertet den Spielstand
    mit `minmax` aus. Der Rückgabewert ist der Zug als String"""
    possiblemoves = possible_moves(bordlist)
    best_result = -2 # Kleiner Startwert, damit jeder echter Minimax-Score besser ist
    best_move = None

    if bot_playernumber=="player1": 
        bot_playersymbol = "X"
    else:
        bot_playersymbol = "O"
    
    for x in possiblemoves: #alle möglichen Züge durchgehen
        simulation_bord = copy.deepcopy(bordlist) #Kopiert das bord, damit das Originale nicht verändert wird
        simulation_bord[x[0]][x[1]] = bot_playersymbol #Zug auf dem Simulationsbord setzen
        minimax_result = minmax(simulation_bord, bot_playernumber[-1:], False) #False, da wir ja einmal in der simulation_difficult() manuell einen maxwert herausgearbeitet haben

        if minimax_result > best_result: #beste Bewertung merken
            best_result = minimax_result
            best_move = bordlist[x[0]][x[1]]
    return best_move

def minmax(bordlist:list, bot_playernumber:str, maximizingPlayer):
    "mithilfe des Minimax Algorithmus wird der Spielstand bewertet"
    symbol = {"1":"X", "2":"O"}
    possible_move = possible_moves(bordlist) 

    #wintest
    won_bot =  wintest(bordlist,"player"+bot_playernumber) 
    won_player = wintest(bordlist,"player"+("1" if bot_playernumber=="2" else "2"))
    if won_bot == True: #verloren
        return 1
    elif won_player == True:#gewonnen
        return -1
    elif len(possible_move) == 0: #unentschieden
        return 0 
    
    if maximizingPlayer: #wollen das best mögliche ergebnis
        maxEval = -100000
        for child in possible_move: # Für jede mögliche Aktion den Spielstand simulieren
            bordlist[child[0]][child[1]] = symbol[bot_playernumber] #spielt simulierten zug für bot 
            eval = minmax(bordlist, bot_playernumber, False) 
            maxEval = max(maxEval, eval) 
            bordlist[child[0]][child[1]] = child[0]*3 + child[1] + 1 #macht den simulierten zug rückgängig
        return maxEval
    
    else: # wollen das schlecht möglichste ergebnis
        minEval = +100000
        for child in possible_move:
            bordlist[child[0]][child[1]] = symbol["1" if bot_playernumber=="2" else "2"]  
            eval = minmax(bordlist, bot_playernumber , True)
            minEval = min(minEval, eval) 
            bordlist[child[0]][child[1]] = child[0]*3 + child[1] + 1 
        return minEval
if __name__ == "__main__": #bordliste zum testen im logic.py file
    # bordliste = [["X", 1 ,"O"],
    #              ["O","O", 5 ],
    #              ["X", 7 ,"X"]]
    bordliste = [["X", "X" , "X" ],
                 [1 ,2 , "X" ],
                 ["O","X","O"]]
    # bordliste = [["O","O","X" ],
    #              ["X", 4 ,"O" ],
    #              [ 6 , 7, "X"]]
    # bordliste = [[0,1,2],
    #              [3,4,5], 
    #              [6,7,8]]
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

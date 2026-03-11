
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
    
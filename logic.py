def output(bordlist):

    ENDC        = "\033[0m"        
    RED         = "\033[91m"
    GREEN       = "\033[92m"
    rowcounter  = 0

    for i in bordlist:
        for y in i:
            if y == "X":
                if rowcounter < 2:
                    print(f'{RED}{y}{ENDC}', end="")
                    print(" | ", end="")
                    rowcounter += 1
                else:
                    print(f'{RED}{y}{ENDC}')
                    rowcounter = 0

            elif y == "O":
                if rowcounter < 2:
                    print(f'{GREEN}{y}{ENDC}', end="")
                    print(" | ", end="")
                    rowcounter += 1
                else:
                    print(f'{GREEN}{y}{ENDC}')
                    rowcounter = 0

            else:
                if rowcounter < 2:
                    print(f'{y}', end="")
                    print(" | ", end="")
                    rowcounter += 1
                else:
                    print(f'{y}')
                    rowcounter = 0

    if wintest(bordlist, "player1") == True:
          print(bordlist)
          print("Spieler 1 hat gewonnen!")

    elif wintest(bordlist, "player2") == True:
          print(bordlist)
          print("Spieler 2 hat gewonnen!")
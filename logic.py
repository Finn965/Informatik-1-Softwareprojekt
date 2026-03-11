def output(boardlist):
    ENDC        = "\033[0m"        
    RED         = "\033[91m"
    GREEN       = "\033[92m"
    rowcounter  = 0

    if wintest(boardlist, player1) == True:
          print(boardlist)
          print("Spieler 1 hat gewonnen!")

    elif wintest(boardlist, player2) == True:
          print(boardlist)
          print("Spieler 2 hat gewonnen!")

    else:
          for i in boardlist:
                for y in i:
                    if y == "X":
                        if rowcounter < 2:
                            print(f'{RED}{y}{ENDC}', end="")
                            print(" | ", end="")
                            rowcounter = rowcounter + 1
                        else:
                            print(f'{RED}{y}{ENDC}')
                            rowcounter = 0

                    elif y == "O":
                        if rowcounter < 2:
                            print(f'{GREEN}{y}{ENDC}', end="")
                            print(" | ", end="")
                            rowcounter = rowcounter + 1
                        else:
                            print(f'{GREEN}{y}{ENDC}')
                            rowcounter = 0

                    else:
                        if rowcounter < 2:
                            print(f'{y}', end="")
                            print(" | ", end="")
                            rowcounter = rowcounter + 1
                        else:
                            print(f'{y}')
                            rowcounter = 0
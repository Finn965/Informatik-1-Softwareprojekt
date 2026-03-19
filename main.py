##########################################################################################
##                                                                                      ##
## Author: Quang Schulz, Fabienne Fechter, Felix Rösch, Finn Dahlmanns, Marvin Gorbach  ##
##                                      11.03.2026                                      ##
##           Play TicTacToe against a bot or in coop against your friends               ##
##                                                                                      ##
##########################################################################################
from logic import input_gamestep, wintest, gamestatus, spielstand, simulation_easy, simulation_medium, simulation_difficult, output, set_move, possible_moves
from menue import hauptmenue



#creating a list for the game board - output in the terminal
BORDLIST = [ [0,  1 , 2 ], 
             [3 , 4 , 5 ],
             [6 , 7 , 8 ]]

# giving variables for the different turns
Player1_turn = False


def main():
    programmläuft = True
    Spieler1 = 0
    Spieler2 = 0
    while programmläuft:
        modus, schwierigkeit = hauptmenue() # Hauptmenü aufrufen und Spielmodus sowie Schwierigkeit zurückgeben
        bordlist = [row[:] for row in BORDLIST]
        output(bordlist)
        Player1_turn =True
        aktuelles_Spiel = True
        unentschieden = False
        while aktuelles_Spiel:   #Spielstart
            if modus == "ki" and gamestatus(bordlist)==0: #wenn Spieler gegen KI spielt
                if Player1_turn and wintest(bordlist,"player2")==False: #Spieler 1 ist dran
                    if possible_moves(bordlist)!= []:
                        move= input_gamestep(bordlist,1) # Spieler 1 macht einen Zug
                        bordlist = set_move(bordlist,"X", move) # Zug auf dem Spielbrett setzen
                        Player1_turn = False
                        output(bordlist)
                    else: 
                        print("Untentschieden")
                        unentschieden = True


      
                elif gamestatus(bordlist)==0: # Bot macht sein Zug
                    print("\nZug vom Bot:\n")
                    if schwierigkeit == "leicht":     #Für Schwierigkeitsstufe leicht
                        move = simulation_easy (bordlist)
                        bordlist = set_move(bordlist,"O",move)
                        Player1_turn = True
                        output(bordlist)
                    if schwierigkeit == "mittel": #Für Schwierigkeitsstufe mittel
                        move = simulation_medium(bordlist,"player2")
                        bordlist = set_move(bordlist,"O",move)
                        Player1_turn = True
                        output(bordlist)
                    if schwierigkeit == "schwer": # Für Schwierigkeitsstufe schwer
                        move = simulation_difficult (bordlist,"player2")
                        bordlist = set_move (bordlist,"O",move)
                        Player1_turn = True
                        output(bordlist)

            if modus == "coop" and gamestatus(bordlist)==0:# Coop- Funktion
                if possible_moves(bordlist)!=[]:      # für unentschieden
                    if Player1_turn and gamestatus(bordlist)==0: # Spieler 1 am Zug
                        move =input_gamestep(bordlist,1)
                        bordlist = set_move (bordlist,"X",move)
                        Player1_turn = False
                        output(bordlist)
                        
                    elif Player1_turn == False and gamestatus(bordlist)==0: # Spieler 2 am Zug
                        move =input_gamestep(bordlist,2)
                        bordlist = set_move (bordlist,"O",move)
                        Player1_turn = True
                        output(bordlist)
                else: 
                    print("Untentschieden")
                    unentschieden = True

            if gamestatus(bordlist)!=0 or unentschieden == True:
                aktuelles_Spiel = False
                print("\nAktueller Spielstand:")
                if gamestatus(bordlist)==1:
                    Spieler1 = spielstand (1,Spieler1)
                elif gamestatus(bordlist)==2:
                    Spieler2 = spielstand(2,Spieler2)
                elif unentschieden:
                    Spieler2+=1
                    Spieler1+=1
                print("Spieler 1:", Spieler1)
                print("Spieler 2:", Spieler2)
                while True:
                    nochmal = input ("Willst du noch eine Runde spielen? (ja/nein)")
                    if nochmal == "ja":
                        print("Neue Runde startet")
                        break
                    elif nochmal == "nein":
                        print("Programm beendet")
                        programmläuft = False
                        break
                    else: 
                        print ("Ungültige Eingabe. Bitte gib ja ode nein ein.")

                        

if __name__ == "__main__":
    main()
                    

                    


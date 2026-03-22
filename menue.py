GRUEN = '\033[92m'
GELB = '\033[93m'
ROT = '\033[91m'
BLAU = '\033[96m'
RESET = '\033[0m'

def hauptmenue():
    # Krasse ASCII-Art für den Titel des Spiels
    
    print(f"{BLAU}")
    print("  _____ _        _____           _____          ")
    print(" |_   _(_)      |_   _|         |_   _|         ")
    print("   | |  _  ___    | | __ _  ___   | | ___   ___ ")
    print("   | | | |/ __|   | |/ _` |/ __|  | |/ _ \\ / _ \\")
    print("   | | | | (__    | | (_| | (__   | | (_) |  __/")
    print("   \\_/ |_|\\___|   \\_/\\__,_|\\___|  \\_/\\___/ \\___|")
    print(f"{RESET}")

    # Der unfassbar coole Rahmen für das Hauptmenü
    print(f"{BLAU}╔════════════════════════════════════════╗{RESET}")
    print(f"{BLAU}║{RESET}      Willkommen beim Tic-Tac-Toe!      {BLAU}║{RESET}")
    print(f"{BLAU}╚════════════════════════════════════════╝{RESET}")

    modus = ""
    # Eingabevalidierung für den Spielmodus
    while modus not in ["1", "2"]:
        print(f"\n{BLAU}--- Bitte wähle den Spielmodus ---{RESET}")
        print("[1] Co-op (Spieler vs. Spieler)")
        print("[2] KI (Spieler vs. Computer)")
        modus = input("Eingabe (1 oder 2): ")

        if modus not in ["1", "2"]:
            print(f"{ROT}Ungültige Eingabe! Bitte gib 1 oder 2 ein.{RESET}")

    if modus == "1":
        print(f"\n{GRUEN}--> Spielmodus: Co-op gestartet!{RESET}\n")
        return "coop", None
    
    elif modus == "2":
        schwierigkeit = ""
        # Eingabevalidierung für die KI-Schwierigkeit
        while schwierigkeit not in ["1", "2", "3"]:
            print(f"\n{BLAU}--- Bitte wähle die KI-Schwierigkeit ---{RESET}")
            print("[1] Leicht")
            print("[2] Mittel")
            print("[3] Schwer")
            schwierigkeit = input("Eingabe (1, 2 oder 3): ")

            if schwierigkeit not in ["1", "2", "3"]:
                print(f"{ROT}Ungültige Eingabe! Bitte gib 1, 2 oder 3 ein.{RESET}\n")


        if schwierigkeit == "1":
            print(f"{GRUEN}Du hast den Spielmodus 'KI - Leicht' gewählt! Viel Spaß!{RESET}")
            return "ki", "leicht"
        elif schwierigkeit == "2":
            print(f"{GRUEN}Du hast den Spielmodus 'KI - Mittel' gewählt! Viel Spaß!{RESET}")
            return "ki", "mittel"
        elif schwierigkeit == "3":
            print(f"{GRUEN}Du hast den Spielmodus 'KI - Schwer' gewählt! Viel Spaß!{RESET}")
            return "ki", "schwer"
        
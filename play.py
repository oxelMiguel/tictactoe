from function import *
from class1 import joueur
import time

# fonction pour afficher le message de demarrage
start()
# on recupere le mode de jeux | deux joueur ou contre IA
mode = menu()

if mode == 1:  # si le mode deux joueur est selectionné le code suivant est executé
    jouInfo = creerJoueur()  # la fonction creer joueur renvoie une liste contenant les noms
                             # et les symboles de chaque joueur
    print("Le jeux peux commencer !!!")
    print(" ")
    afficher()  # afficher la grille
    joueur1 = joueur(jouInfo[0], jouInfo[1])  # on crée un objet joueur1 contenant les infos du premier joueur
    joueur2 = joueur(jouInfo[2], jouInfo[3])  # on crée le joueur 2

    while " " in board:  # tant que la grille n'est pas plein on execute le code suivant

        pos = int(input(f"{joueur1.nom} : "))
        sucess = 0
        while sucess == 0:
            sucess = set_game(pos, joueur1.symbole)
            if sucess == 0:
                pos = int(input("Choisissez une autre position >>>>"))
        if check_winner(joueur1.symbole):
            afficher()
            time.sleep(2)
            print(f"{joueur1.nom} gagne !!!")
            break
        afficher()

        pos = int(input(f"{joueur2.nom} : "))
        sucess = 0
        while sucess == 0:
            sucess = set_game(pos, joueur2.symbole)
            if sucess == 0:
                pos = int(input("Choisissez une autre position >>>>"))
        if check_winner(joueur2.symbole):
            afficher()
            time.sleep(2)
            print(f"{joueur2.nom} gagne !!! ")
            break
        afficher()

if mode == 2:

    lev = int(input("""Veuillez selectionner un niveau :
    
    1) Facile
    2) Normal
    3) Difficile
    
    utiliser le numero >>> """))

    while lev not in [1, 2, 3]: lev = int(input("Choississez un niveau valide >>>"))

    print(" ")
    nom1 = input("Entrez votre nom >>>>")
    syn1 = choose_syn()
    print(" ")

    player = joueur(nom1, syn1)

    if syn1 == "0":
        synA = "x"
    else:
        synA = "0"
    IA = "IA"

    while " " in board:

        pos = int(input(f"{player.nom} : "))
        sucess = 0
        while sucess == 0:
            sucess = set_game(pos, player.symbole)
            if sucess == 0:
                pos = int(input("Choisissez une autre position >>>>"))
        if check_winner(player.symbole):
            afficher()
            time.sleep(2)
            print(f"{player.nom} gagne !!!")
            break
        afficher()

        if lev == 1:
            pos = chose(player.symbole, synA)

        print(f"{IA} : {pos}")
        sucess = set_game(pos, synA)

        if check_winner(synA):
            afficher()
            time.sleep(2)
            print(f"{IA} gagne !!! ")
            break
        afficher()

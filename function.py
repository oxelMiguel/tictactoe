import time
import random
board = [" "," "," "," "," "," "," "," "," "]

def afficher():
    print("_____________")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4]  + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7]  + " | " + board[8] + " |")
    print("-------------")
    print(" ")

def not_empty(pos):
    if board[pos - 1] == " ":
        return True
    else:
        return False

def set_game(pos,char):

    if (not_empty(pos)):
        board[pos-1]=char
        sucess = 1
        return sucess
    else:
        sucess = 0
        print("  ")
        print("position deja occupé")
        return sucess




"""afficher()
while " " in board :
    pos=int(input("entrez la position"))
    set_game(pos,"x")
    afficher()"""

def start():


    print("""
    Alignement du tableau:

    | 1 | 2 | 3 | 
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |

    """)

    print("Utiliser les chiffres pour choisir votre position")
    print("Vous gagnez losque vous allignez vos trois synbole sur la vertical,en horizontale ou en diagonale")

def level():
    lev=int(input(
        """
        Veuillez selectionner le niveau de jeu :
        
        1) Facile
        2)Normale
        3)Difficile
        
        >>>>"""

    ))

    return lev

def choose_syn():
    sym=input(
        """
        Veuillez choisir votre symbole : 0 ou X
        >>>>"""
    )

    while sym not in ["0","X"]:
        sym=input("veuillez choisir un symbole valide : (0 ou X) >>>>")



    return sym


def menu():
    print(" ")
    print("Choisissez votre mode de jeux :")
    md=0
    while md not in[1,2] :
        md=int(input("""
        1) Jouer à deux 
        2) Jouer contre l'ordinateur
        >>>>"""))
    return md


def creerJoueur():
    print(" ")
    print("Joueur 1 :")
    nom1 = input("Entrez votre nom >>>>")
    syn1 = choose_syn()
    print(" ")
    print("Joueur 2 : ")
    nom2 = input("Entrez votre nom >>>>")
    if syn1 == "0":
        syn2="X"
    else:
        syn2="0"
    print(" ")
    time.sleep(1)
    print("Votre symbole est " + syn2)
    time.sleep(1)
    print(" ")

    return [nom1,syn1,nom2,syn2]


def check_winner(ch):

    v1 = board[:3]
    v2 = board[3:6]
    v3 = board[6:]
    h1 = board[:8:3]
    h2 = board[1:8:3]
    h3 = board[2::3]
    d1 = board[::4]
    d2 = board[2:8:2]
    win_pattern = [ch, ch, ch]
    winlist = [v1, v2, v3, h1, h2, h3, d1, d2]

    if win_pattern in winlist:
        return True
    else:
        return False



def chose(symJ1,symA):
    v1 = board[:3]
    v2 = board[3:6]
    v3 = board[6:]
    h1 = board[:8:3]
    h2 = board[1:8:3]
    h3 = board[2::3]
    d1 = board[::4]
    d2 = board[2:8:2]

    case = [v1,v2,v3]
    j = 0
    i=0
    while j<=3:
        if case[j] == [symJ1, " ", " "] :
            l = [2,3]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [" ", symJ1, " "] :
            l = [1, 3]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [" ", " ", symJ1] :
            l = [1, 2]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [symJ1, symJ1, " "] :
            l = [3]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [symJ1, symA, " "] :
            l = [3]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [symJ1, " ", symA] :
            l = [2]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [" ", symJ1, symA] :
            l = [1]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [symA, symJ1, " "] :
            l = [3]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [" ", symA, symJ1] :
            l = [1]
            return i + l[random.randrange(len(l))]
            break
        elif case[j] == [" ", " ", " "] :
            l = [1, 2, 3]
            return i + l[random.randrange(len(l))]
            break

        i+=3
        j+=1
        continue

























from bibliotheque_tic_tac_toe import *

def test():
    if test_win(JOUEUR, CARTE):
        stdout.write("Victoire du joueur !!!\n")
        return False
    if test_win(IA, CARTE):
        stdout.write("Victoire de l'IA !!!\n")
        return False
    if test_fin(CARTE):
        print("Match nul !!!")
        return False
    return True
def tour():
    if T == 1:
        joueur_tour()
        afficher_jeu()
        a = test()
        if a == False:
            return False
        b = ia_tour()
        afficher_jeu()
    if T == 2:
        ia_tour()
        afficher_jeu()
        a= test()
        if a == False:
            return False
        b = joueur_tour()
        afficher_jeu()
    return test()

def joueur_tour():
    ERREUR = True
    # Tour Joueur
    while ERREUR:
        stdout.write("> ")
        try : 
            i = int(stdin.readline()) - 1
        except:
            i = -1
        if 0 <= i < DIM**2:
            x, y = i//DIM , i%DIM
            if CARTE[x][y].isdigit():
                CARTE[x][y] = JOUEUR
                ERREUR = False
    
    return True

def ia_tour():
    carte = deepcopy(CARTE)
    x,y = best_mouv(carte)
    try:
        CARTE[x][y] = IA
    except:
        pass

def afficher_jeu():
    
    stdout.write("----------\n")
    for ligne in CARTE:
        stdout.write("%s\n" %" ".join(ligne))
    
def main():
    global CARTE, T
    CARTE = [[str(DIM*l+i) for i in range(1,DIM+1)] for l in range(DIM)]

    # Premier au deuxième joueur ?
    stdout.write("1 ou 2 ? > ")
    T = stdin.readline()
    if T == "1\n" or T == "2\n":
        T = int(T)
    else:
        T = 1

    # Jeux
    afficher_jeu()
    while tour():
        pass
while True:
    main()

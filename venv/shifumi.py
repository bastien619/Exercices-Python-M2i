"""
Jeu : shifumi
Le jeu propose à deux joueurs de s'affronter sur un duel Shifumi
le premier arriver à trois à gagner la partie
cependant la partie continue tant qu'il n'y a pas 2 points d'écarts
"""



def shifumi ():
    sc1,sc2 = 0,0
    while (sc1 < 3 and sc2 < 3) or abs(sc1 - sc2) < 2:
        print("Joueur A, a vous de jouer")

        j1 = int(input("1 -> pierre \n 2 -> papier \n 3 -> ciseaux : "))
        while not 1 <= j1 <= 3 :
            print("l'entrée n'est pas valide")
            print("Joueur A, a vous de jouer")
            j1 = int(input("1 -> pierre \n 2 -> papier \n 3 -> ciseaux : "))


        print("Joueur B, a vous de jouer")
        j2 = int(input("1 -> pierre \n 2 -> papier \n 3 -> ciseaux : "))
        while not 1 <= j2 <= 3:
            print("l'entrée n'est pas valide")
            print("Joueur B, a vous de jouer")
            j2 = int(input("1 -> pierre \n 2 -> papier \n 3 -> ciseaux : "))

        if (j1 == j2):
            print("egalité")
        elif (j1 % 3) + 1 == j2:
            sc2 += 1
            print(f"Le Joueur B gagne la manche \n les scores sont de : \n Joueur 1 -> {sc1} \n Joueur 2 -> {sc2}")
        else:
            sc1 += 1
            print(f"Le Joueur A gagne la manche \n les scores sont de : \n Joueur 1 -> {sc1} \n Joueur 2 -> {sc2}")

    print("Le joueur A à gagné") if sc1 > sc2 else print("Le joueur B à gagné")

#shifumi()
# _*_ coding:Utf8 _*_
#Exercice : Nombre magique avec l'utilisation de break.... si on rentre un nombre negatif on sort du programme avec un message
#"vous avez abandonné le jeu"
x = 0
target = 7

while (x != target) :
    x = int(input("Entrez un chiffre entre 0 et 100: \n"))
    if x < 0 :
        print("Jeu abandonné")
        break
    elif x > 100 :
        print("Chiffre en dehors des bornes")
    elif x < target :
        print("Chiffre trop petit")
    else :
         print("Bonne réponse!") if x == target else print("Chiffre trop grand")


#Exercice :
#proposer 3 programmes
#calculer l'air d'un carre
#le volume d'une sphere
#le volume d'un parallépipède
#help (il faut importer math avec l'utilisation de math.pi)
import math

def square_area(x) :
    return x**2

def volume_sphere(r) :
    return (4/3)*math.pi*(r**3)

def volume_parallepipede(a,b,c) :
    return a*b*c


carrS = int(input("Entrez la longueur du coté du carré : \n"))
print(f"L'aire du carré est de {square_area(carrS)}\n")
sphereR = int(input("Entrez le rayon de la sphère : \n"))
print(f"Le volume de la sphère est de {volume_sphere(sphereR)}\n")
paraA = int(input("Entrez la longueur du parallèpipède : \n"))
paraB = int(input("Entrez la largeur du parallèpipède : \n"))
paraC = int(input("Entrez la hauteur du parallèpipède : \n"))
print(f"Le volume du parallèpipède est de {volume_parallepipede(paraA,paraB,paraC)}\n")


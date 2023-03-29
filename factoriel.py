# _*_ coding:Utf8 _*_
#Exercice : ecrire une factorielle en iteratif
#pour une chaine de caracteres, determine par recursivite sa longueur


#rendre recursif
def somme(L):
s=0 :
for val in L :
s+=val
return s

#Ecrire une fonction récursive « Binaire » permettant d’imprimer à l’écran la représentation binaire d’un nombre N.


#ecrire la suite de Fibonacci en récursif fib(n)

#la factorielle

#donner un nombre et determiner tous les nombres premiers précédents.

#ecrire un programme qui determine si un mot est un palindrome.
n = int(input("Entrez un chiffre : \n"))
print("{}! = ".format(n), end="")


def factoriel(n) :
    if n == 1 :
        return 1
    else :
        return n*factoriel(n-1)
# _*_ coding:Utf8 _*_
#Exercice table de multiplication : le programme demande la table, la valeur maximal du multiplicateur, le pas de calcul

table = int(input("Entrez la table de multiplication a calculer : "))
nmax = int(input("Entrez jusqu'où la table s'arrete : "))
pas = int(input("Entrez le pas de la table : "))

for x in range(1,nmax+1,pas) :
    print(table,"x",x,"=",table*x)



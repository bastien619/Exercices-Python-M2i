from math import pi

def somme_pi(n) :
    if n <= 1 :
        return 1
    else :
        return somme_pi(n-1) + 1/(n**2)

def somme_pi2(n) :
    somme = somme_pi(n)
    print("Valeur de la somme :", somme)
    print("π²/6 = ", (pi**2)/6)
    print("Ecart de {:.2f}% par rapport à π²/6".format(abs( (somme - (pi**2)/6) /( (pi**2)/6) * 100)))

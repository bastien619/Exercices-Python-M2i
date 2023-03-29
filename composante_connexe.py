import random
def finder(l) :
    for enum in enumerate(l) :
        if enum[1] == 1 :
            return enum[0]
    return -1


def compConnexe(l,k,x=1) :
    if k >= 0 :
        l[k] = x
        if k < len(l)-1:
            if l[k+1] == 1 :
                compConnexe(l,k+1,x+1)
            else :
                kn = finder(l[k+1:])
                if kn >= 0 :
                    compConnexe(l, kn + k + 1, 1)



def compInit(l) :
    print(l)
    compConnexe(l,finder(l),1)
    print(l)

l=[random.randint(0,1) for i in range(30)]
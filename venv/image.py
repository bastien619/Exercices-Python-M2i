import random as rd
import matplotlib.pyplot as plt

nx = int(input("Longeur de l'image : "))
ny = int(input("Largeur de l'image : "))
image = []

for i in range(nx) :
    image.append([rd.randint(0,1) for i in range(ny)])

def etiquetter(image) :
    T = 2
    for i in range(len(image)) :
        for j in range(len(image[i])) :
            if image[i][j] == 1 :
                propager(image,i,j,T)
                T += 1

def propager(image,i,j,T) :
    image[i][j] = T
    if i > 0 and image[i-1][j] == 1 :
        propager(image,i-1,j,T)
    if i < len(image)-1 and image[i+1][j] == 1 :
        propager(image,i+1,j,T)
    if j > 0 and image[i][j-1] == 1 :
        propager(image,i,j-1,T)
    if j < len(image[0])-1 and image[i][j+1] == 1 :
        propager(image,i,j+1,T)


for i in range(nx) :
    for j in range (ny) :
        print(image[i][j], end=" ")
    print()
print("\n")


etiquetter(image)
for i in range(nx) :
    for j in range (ny) :
        print(image[i][j], end=" ")
    print()

plt.matshow(image)
plt.show()



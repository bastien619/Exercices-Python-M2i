import random as rd

#Calcule la moyenne d'une liste de nombres
def avg(lst):
    return sum(lst) / len(lst)


nb_eleves = int(input("Entrez le nombre d'élèves : ")) #Nombre d'élèves

nb_matieres = int(input("Entrez le nombre de matières : ")) #Nombre de matières
notes = []

#Entrée de toutes les notes aléatoirement
for i in range(nb_matieres) :
    nb_notes = rd.randint(2,5)
    notes.append([])
    for j in range(nb_eleves) :
        notes[i].append([round(rd.gauss(12,3)) for i in range(nb_notes)])


eleve_mat_note_max = [0,0,0] #Meilleure note de la classe tout matières confondue
eleve_mat_note_min = [0,0,20] #Pire note de la classe tout matières confondue
moyenne_classe = 0 #Moyenne de la classe

#Affichages des résultats
for j in range(nb_eleves) :
    moyennes = [] #Moyennes par matière de l'élève j
    print(f"Eleve {j+1} :")
    for i in range(nb_matieres) :
        print(f"    Matière {i+1} :")

        maxi = max(notes[i][j]) #Meilleure note de l'élève j dans la matière i
        print(f"        Meilleure note : {maxi}")
        if maxi > eleve_mat_note_max[2] :
            eleve_mat_note_max = [j,i,maxi]

        mini = min(notes[i][j]) #Pire note de l'élève j dans la matière i
        print(f"        Pire note : {mini}")
        if mini < eleve_mat_note_min[2] :
            eleve_mat_note_min = [j,i,mini]

        moyennes.append(avg(notes[i][j])) #Moyenne de l'élève j dans la matière i
        print(f"        Moyenne : {round(moyennes[i],2)}")

    moyenne_generale = avg(moyennes) #Moyenne générale de l'élève j
    print(f"    Moyenne générale : {round(moyenne_generale,2)}\n")
    moyenne_classe += moyenne_generale

moyennes_classe = moyenne_classe / nb_eleves #Moyenne générale de la classe

print(f"Moyenne générale de la classe : {round(moyennes_classe,2)}")
print(f"Meilleure note de la classe : {eleve_mat_note_max[2]} par l'élève {eleve_mat_note_max[0]+1} dans la matière {eleve_mat_note_max[1]+1}")
print(f"Pire note de la classe : {eleve_mat_note_min[2]} par l'élève {eleve_mat_note_min[0]+1} dans la matière {eleve_mat_note_min[1]+1}")

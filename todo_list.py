todo = {
    "Lessive" : "Finir de laver les assiettes",
    "Menage" : "Passer l'aspirateur dans le salon et dépoussierer les armoires",
    "Cuisine" : "Acheter les ingéredients pour un chili con carne"
}
choix = 1

while choix != 4 :
    choix = int(input("### Menu ###\n1) Ajout d'un todo\n2) Execution d'un todo\n3) Affichage de la todolist\n4) Quitter\n"))
    match choix:
        case 1 :
            k = input("Nom de la tache : ")
            v = input("Contenu de la tache : ")
            todo[k] = v
        case 2 :
            k = input("Tache a éxecuter : ")
            if k in todo.keys() :
                print(todo.pop(k),"\n")
            else :
                print("Cette tache n'est pas dans la liste\n")
        case 3 :
            for (k,v) in todo.items() :
                print(k,":",v)
            print()
        case 4:
            print("Au revoir!")
        case _:
            print("Choix non valide")



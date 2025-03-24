


def tab(nb_of_lignes): #construction d'un tableau vide ( valeurs 0 )
    Liste_def = []
    for x in range(nb_of_lignes):
        Liste_def.append([])
        for y in range(nb_of_lignes):
            Liste_def[x].append(0)
    return Liste_def

def afficher_tab(tab):  #affichage d'un tableau
    for x in range(len(tab)):
        for y in range(len(tab[x])):
            print(" ",tab[x][y], end='')
        print()
    

def tab_cout(list):     #doit être transformé au préalable
    liste_cost = []
    for x in range(len(list)): # lignes 
        liste_cost.append(list[x][1])
    print(liste_cost)
    return liste_cost

def afficher_ligne(tab):
    for ligne in tab:       
        for x in range(len(ligne)):
            print(ligne[x])
            print(x)
        print(end='')

#la transformation en question   
def transform_to_tab(lignes): #enlève les espaces et met le tableau sous la forme (ligne/cout/list de prédécesseur)
    list = []
    for ligne in lignes:
        list.append(ligne.split())
    print(list)
    return list

#on ajoute les valeurs avec les coûts dans le tableau final
def put_values_in_tab(lignes):
    tabe = transform_to_tab(lignes)
    
    tab_cout_v1 = tab_cout(tabe)
    liste_final = tab(len(lignes)+1)
    print("tab vite avant les valeurs")
    afficher_tab(liste_final)
    for x in range(len(tabe)):
        print("numéro de lignes",x,"len",len(tabe))
        for y in range(2,len(tabe[x])):
            print("tabe",len(tabe[x]))
            print("valeurs pour",y,'taille de tabe[x]',len(tabe))
            print(liste_final[y][x],y,x)
            print("valeur de tabe",tabe[x][y])
            print(tab_cout_v1[x])
            liste_final[int(tabe[x][y])][x]=tab_cout_v1[int(tabe[x][y])-1]
    print("après valeurs et coût mis")
    return liste_final





def main():
    f = open('data.txt', 'r')
    lignes = f.readlines()  # Retourne une liste
    for ligne in lignes:
        print(ligne)
    tab = put_values_in_tab(lignes)
    afficher_tab(tab)
    
    

main()

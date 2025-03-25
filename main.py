from sommet import *
from verification import *

def tab(nb_of_lignes): #construction d'un tableau vide ( valeurs 0 )
    Liste_def = []
    for x in range(nb_of_lignes):
        Liste_def.append([])
        for y in range(nb_of_lignes):
            Liste_def[x].append('.')
    return Liste_def

def afficher_tab(tab):  #affichage d'un tableau
    for i in range(0,len(tab)):
        if (i==0):
            print("     a ",end="")
        elif i==(len(tab)-1):
            print(" o ",end="")
        else:
            if i>=10:
                print(i,"",end="")
            else:
                print("",i,end=" ")
    print()
    for x in range(len(tab)):
        if (x==0):
            print("a  ",end="")
        elif x==(len(tab)-1):
            print("o  ",end="")
        else:
            if x>=10:
                print(x,"",end="")
            else:
                print(x," ",end="")
        for y in range(len(tab[x])):
            print(" ",tab[x][y], end='')
        print()
    

def tab_cout(list):     #doit être transformé au préalable
    liste_cost = []
    for x in range(len(list)): # lignes 
        liste_cost.append(list[x][1])

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

    return list

#on ajoute les valeurs avec les coûts dans le tableau final
def put_values_in_tab(lignes):
    tabe = transform_to_tab(lignes)
    list_destination = [] #liste qui ont un suivant 
    list_predecesseur = [] #ceux qui ont un précédent 
    tab_cout_v1 = tab_cout(tabe)
    liste_final = tab(len(lignes)+2)
    for x in range(len(tabe)):
        for y in range(2,len(tabe[x])):
            liste_final[int(tabe[x][y])][x+1]=tab_cout_v1[int(tabe[x][y])-1]
            if (x+1) not in list_predecesseur:
                list_predecesseur.append(x+1)
            if int(tabe[x][y]) not in list_destination:
                list_destination.append(int(tabe[x][y]))

    for z in range(1,len(liste_final[0])-1):
        if z not in list_predecesseur:
            liste_final[0][z]='0'
    for i in range(1,len(liste_final[0])-1):
        if i not in list_destination:
            b = len(liste_final)-1
            liste_final[i][b]=tab_cout_v1[i-1]
    return liste_final





def main():

    f = open('data.txt', 'r')
    lignes = f.readlines()  # Retourne une liste
    tab = put_values_in_tab(lignes)
    afficher_tab(tab)
    #print(verif_circuit(tab))
    #print(verif_arc_neg(tab))
    rang_sommet(tab)
    
    
    

main()

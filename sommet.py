

def rang_sommet(tab):
    list_de_rang = [] #liste de rang final
    exit = False
    tab_copie=tab #copie de travail, car modification à venir 
    while exit!=True:
        list_de_rang_temp=[] #liste de rang qu'on ajoutera à chaque itération à liste de rang
        list_pred_temp = [] #liste de prédécessuer temporaire, par itération
        for x in range(len(tab_copie)):
            for y in range(len(tab_copie)):
                if tab_copie[x][y] !='X':
                    print(tab_copie[x][y])
                    list_pred_temp.append(tab_copie[x][y])
        print(list_pred_temp)
        for i in range(len(tab_copie)):
            if i not in list_pred_temp:
                list_de_rang_temp.append(i)
                for o in range(len(tab_copie)):
                    tab_copie[i][o]='X'
        #afficher_tab(tab_copie)
        list_de_rang.append(list_de_rang_temp)
        if list_pred_temp==[]:
            exit=True
    print(list_de_rang)
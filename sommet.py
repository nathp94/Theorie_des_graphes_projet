

def jesuisdanstamatrice(list,n):
    for x in range(len(list)):
        for y in range(len(list[x])):
            if list[x][y]==n:
                return True
    return False  


def rang_sommet(tab):
    list_de_rang = [] #liste de rang final
    exit = False
    tab_copie=tab
    print("tabcopie",tab_copie) #copie de travail, car modification à venir 
    print("tab",tab)
    while exit!=True:
        list_de_rang_temp=[] #liste de rang qu'on ajoutera à chaque itération à liste de rang
        list_pred_temp = [] #liste de prédécessuer temporaire, par itération
        for x in range(len(tab_copie)):
            for y in range(len(tab_copie)):
                print(tab_copie[x][y])
                if tab_copie[x][y] !='.':
                    print(tab_copie[x][y])
                    print("ICIIIIIII")
                    list_pred_temp.append(y)
        print(list_pred_temp)
        for i in range(len(tab_copie)):
            if i not in list_pred_temp:
                if jesuisdanstamatrice(list_de_rang,i)==False:
                    list_de_rang_temp.append(i)
                for o in range(len(tab_copie)):
                    tab_copie[i][o]='.'
        #afficher_tab(tab_copie)
        list_de_rang.append(list_de_rang_temp)
        if list_pred_temp==[]:
            exit=True
    print(list_de_rang)
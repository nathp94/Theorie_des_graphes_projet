def predecesseur(tab,sommet):
    liste = []
    for i in range(len(tab)):
        if (tab[i][sommet] != 'X') and (i!=sommet):
            liste.append(i)
    return liste

def successeur(tab,sommet):
    liste = []
    for i in range(len(tab)):
        if (tab[sommet][i] != 'X') and (i!=sommet):
            liste.append(i)
    return liste

def verif_circuit(tab):

    # On fait la fermeture transitive sur graphe
    fermeture_transitive = tab
    for i in range(len(tab)):
        for j in predecesseur(tab,i):
            for k in successeur(tab,i):
                fermeture_transitive[j][k] = '1'

    #On regarde la diagonale
    for i in range(len(fermeture_transitive)):
        if fermeture_transitive[i][i]!='X':
            return True

    return False




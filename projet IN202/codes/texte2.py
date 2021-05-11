# texte à déchiffrer:

message= "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."


# méthode de chiffrement utilisée: substitution alphabétique.


# on commence par une analyse des fréquences d'apparition de chaque lettre:


def frequence(message_chiffre):
    """renvoie la fréquence d'apparition de chaque lettre dans le message_chiffre"""
    resultat = []
    for lettre in message_chiffre:
        if 97 <= ord(lettre) <= 122:
            exist = True
            for i in range(len(resultat)):
                if resultat[i][0] == lettre:
                    exist = False    
            if exist:
                resultat.append([lettre, round(message_chiffre.count(lettre)/len(message_chiffre)*100,2)])
    return resultat 

#print(frequence(message))

# fréquences des lettres:
# [['x', 15.93], ['i', 7.52], ['u', 7.52], ['g', 6.19], ['k', 4.87], ['d', 4.87], ['c', 4.87], ['o', 4.42], 
# ['s', 4.42], ['n', 4.42], ['v', 3.54], ['y', 2.65], ['f', 2.21], ['q', 2.21], ['w', 1.33], ['l', 1.33], ['m', 0.88], ['a', 0.44]]

# en comparant ces fréquences aux fréquences d'apparition de chaque lettre dans la langue française, on peut avoir une idée de la 
# substitution de quelques lettres comme (x -> e), (i-> s), (a->z) etc...


def dechiffre(message_chiffre):
    """associe à chaque lettre du message_chiffre la lettre du message_original qui lui correspond"""
    lettres_message_chiffre = ["x","u","i","g","k","d","c","n","o","s","v","y","f","q","l","w","m","a"]
    lettres_message_original = ["e","t","s","l","i","n","d","a","r","o","c","u","m","p","h","f","g","z"]
    res = ""
    for lettre in message_chiffre:
        if lettre in lettres_message_chiffre:
            res += lettres_message_original[lettres_message_chiffre.index(lettre)]
        else:
            res+= lettre    
    return res

print("le message déchiffré est:", dechiffre(message))


# texte déchiffré: 
# le prochain fichier est code par un mot de passe de taille inconnue et contient l'indice. 
# les lettres du mot de passe permettent de decaler les lettres du message original modulo 26. 
# seules les lettres de a a z sont chiffrees.
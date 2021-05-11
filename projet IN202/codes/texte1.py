#Texte à déchiffrer:
message = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."

# méthode de chiffrement: chiffrement par décalage à l'aide d'une clé 



# on commence par une alanyse des fréquences d'apparition de chaque lettre:

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
# [['k', 4.85], ['d', 15.76], ['o', 3.64], ['q', 7.88], ['n', 3.03], ['b', 4.24], ['g', 2.42], ['z', 7.27], ['h', 4.85], 
# ['m', 3.03], ['e', 1.21], ['t', 6.67], ['c', 2.42], ['r', 4.85], ['a', 1.21], ['s', 6.67], ['p', 1.82], ['l', 1.21], ['f', 0.61]]

# on remarque que la lettre qui apparait le plus est 'd', on peut donc supposer qu'elle correspond à un 'e', lettre qui apparait 
# le plus dans la langue française. De plus, on remarque plusieurs mots comme "kd, kz", qui peuvent correspondre à 'le, la'
#  le 'k' peut alors correspondre à un 'l'. D'après ces hypothèses ont peut alors en déduire que la clé est "b"


# on déchiffre alors le message en se servant de fonctions:


def rang(lettre): 
    """renvoi un nombre de 0 à 25 à chaque lettre de l'alphabet"""
    return ord(lettre) - 97 


def decalage(lettre_message,lettre_cle):
    """décale une lettre du message par une de la cle"""
    if 97 <= ord(lettre_message)<= 122:
        return chr((rang(lettre_message)+ rang(lettre_cle))%26+ 97 )
    else: 
        return lettre_message


def dec_texte(texte,cle):
    """décale toutes les lettres du texte par toutes les lettres de la cle"""
    textecod = ""
    j = 0 
    i = 0
    for i in range(len(texte)):
        textecod += decalage(texte[i],cle[i%len(cle)])
    return textecod

print("le message déchiffré est:", dec_texte(message,"b"))

# on obtient:
# le prochain fichier aura un code par substitution alphabetique: chaque lettre est remplacee par une autre. 
# utiliser la frequence des lettres pour decoder le message.

# texte à déchiffrer: 

message = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"


# méthode à utiliser: décalage à l'aide d'un mot de passe de taille inconnu. seules les lettres a à z sont chiffrées.



# on cherche d'abord à connaitre la longueur de la clé: On repère dans le message chiffré des sous chaînes qui se répètent, 
# car ces dernières sont sans doute des mêmes portions du texte original, codées avec la même partie de clé. (exemple: "wy", "ep"). 
# On déduit alors que la clé est de taille 4

# Disons que la clé est formée de 4 lettres: L1, L2, L3, L4
# on remarque aussi que les mots formés d'une unique lettres ("e", "c") sont sans doutes des "a" et les lettre suivies d'apostrophes ("n'", "p'")
#sont probablement des "l'". 
# Ainsi, grace a ces hypotheses on peut deviner quelques lettres de la clé: l2= "l" l3= "e" et on en déduit alors la clé: "clez"


def decalage_inverse(lettre_message,lettre_cle):
    return (chr((((ord(lettre_message)-97) - (ord(lettre_cle)-97)) % 26) + 97))

def dec_texte_inverse(message_chiffre,cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(message_chiffre)):
        if 97 <= ord(message_chiffre[i]) <= 122:
            res += decalage_inverse(message_chiffre[i], cle[i%taille_cle])
        else:
            res += message_chiffre[i]
    return res


print("le message déchiffré est:", dec_texte_inverse(message, "clez"))

#texte déchiffré:
# bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. 
# le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?
# programme utile qui sert à chiffrer et dechiffrer un texte à l'aide d'une clé


def frequence(message_chiffre):
    resultat = []
    existe = False

    for lettre in message_chiffre:
        if 97 <= ord(lettre) <= 122:
            exist = True

        for i in range(len(resultat)):
            if resultat[i][0] == lettre:
                exist = False
                    
        if exist == True:
            resultat.append([lettre, round(message_chiffre.count(lettre)/len(message_chiffre)*100,2)])
    
    return resultat 


import tkinter as tk

def decalage(lettre_message,lettre_cle):
    """renvoie le decalage de la premiere lettre par la deuxieme dans l'alphabet de a a z """
    return (chr((((ord(lettre_message)-97) + (ord(lettre_cle)-97)) % 26) + 97))

def dec_texte(texte,cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(texte)):
        if 97 <= ord(texte[i]) <= 122:
            res += decalage(texte[i], cle[i%taille_cle])
        else:
            res += texte[i]
    return res

def chiffre():
    resultat.delete(0,tk.END)
    text=entree_texte.get()
    cle=entree_cle.get()
    res = ""
    if((len(text)>0) and (len(cle)>0)):
        res = dec_texte(text,cle)
        resultat.insert(0,res)
    else:
        resultat.insert(0,"Il manque quelque chose")

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

def dechiffre():
    resultat.delete(0,tk.END)
    message_chiffre = entre_messagechiffre.get()
    cle = entree_cle.get()
    res = ""
    if((len(message_chiffre)>0) and (len(cle)>0)):
        res += dec_texte_inverse(message_chiffre, cle)
        resultat.insert(0,res)
    else:
        resultat.insert(0,"Il manque quelque chose")
    
    return res


racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

entree_cle = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_cle.grid(row = 1, column = 0)

entre_messagechiffre = tk.Entry(racine,width = 50, font = ("helvetica", "20"))
entre_messagechiffre.grid(row=3,column=0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

label_cle = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer la clé ici.")
label_cle.grid(row = 1, column = 1)

label_dech = tk.Label(racine,font = ("helvetica", "20"), text = "Déchiffre ici")
label_dech.grid(row = 3, column = 1)

bouton_coder=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)

bouton_decoder=tk.Button(racine,text="Déchiffrer texte",fg="black",  width=15,command=dechiffre)
bouton_decoder.grid(row=2, column=1)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=4,column=1, columnspan= 4)



racine.mainloop()


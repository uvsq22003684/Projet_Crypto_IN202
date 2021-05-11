# texte à déchiffrer:
# jeqeqecvnf suozvb jfk muj
# dfjr fmy rvuqsk ve
# itajtd mifwz nnrt
# imtrvp zuh srzmzbqz tepr zn
# tmsnirt imtrvp nec hw
# dzpqj tjf pdecpr zl jr
# ptejnt ekpb iu b
# iiuyu iy ijz surg rjs ttsn
# votp ac hw rzpuen jozw
# rvwdvx jbo nirscyjv fi

# svmkyw ve iaflss yie te
# teffvv'u riznxjzvv jfk
# nelrhtjrk dh sivdvjvve
# yi cvb à jffrds tdp
# rvwdv sebr onvnqsy zvp
# zuhjwiM le wmifo wiezib nec
# triot qmjvr'c onrwz
# memfqg srq wdaietsq vk

# Tout d'abord, on remarque que le texte est sans doute a l'enver vu qu'il n'existe pas de mots dans la langue francaise qui terminent 
# par 'u ou 'c ou avec une majuscule.

message_chiffre= "jeqeqecvnf suozvb jfk muj dfjr fmy rvuqsk ve itajtd mifwz nnrt imtrvp zuh srzmzbqz tepr zn tmsnirt imtrvp nec hw dzpqj tjf pdecpr zl jr ptejnt ekpb iu b iiuyu iy ijz surg rjs ttsn votp ac hw rzpuen jozw rvwdvx jbo nirscyjv fi  svmkyw ve iaflss yie te teffvv'u riznxjzvv jfk nelrhtjrk dh sivdvjvve yi cvb à jffrds tdp rvwdv sebr onvnqsy zvp zuhjwiM le wmifo wiezib nec triot qmjvr'c onrwz memfqg srq wdaietsq vk"
mirroir_message_chiffre = message_chiffre[::-1]
print(mirroir_message_chiffre)

# mirroir_message_chiffre: 
# kv qsteiadw qrs gqfmem zwrno c'rvjmq toirt cen bizeiw ofimw el Miwjhuz pvz ysqnvno rbes vdwvr pdt sdrffj à bvc iy evvjvdvis hd krjthrlen kfj vvzjxnzir u'vvffet et eiy sslfai ev wykmvs  
# if vjycsrin obj xvdwvr wzoj neupzr wh ca ptov nstt sjr grus zji yi uyuii b ui bpke tnjetp rj lz rpcedp fjt jqpzd wh cen pvrtmi trinsmt nz rpet zqbzmzrs huz pvrtmi trnn zwfim dtjati ev ksquvr ymf rjfd jum kfj bvzous fnvceqeqej


# on cherche d'abord à connaitre la longueur de la clé: On repère dans le message chiffré des sous chaînes qui se répètent ("nec") 
# on remarque aussi que les mots formés d'une unique lettres ("b") sont sans doutes des "a" et les lettre suivies d'apostrophes ("c'", "u'")
#sont probablement des "l'" ou des "d'"
#on en déduit que la taille de la clé est de 6


#on decoupe notre texte en plusieurs partie par exemple 
# la premiere partie contient les premières lettres de chaque blocs, la deuxième les deuxièmes...

def decoupe_texte(texte): #texte doit etre sans espaces et apostrophes
    res1, res2, res3, res4, res5, res6 = " ", " ", " ", " ", " ", " " 
    i,j = 0,0
    for i in range(0,6):
        for j in range(100):
            if i%6 == 0 and j == 0:
                indice = 0
                res1 += texte[indice]
            else:
                if i + j*6 >= len(texte):
                    break
                else:
                    indice = i+(j*6)
                    if i%6 == 0:
                        res1 += texte[indice]
                    if i%6 == 1:
                        res2 += texte[indice]
                    if i%6 == 2:
                        res3 += texte[indice]
                    if i%6 == 3:
                        res4 += texte[indice]
                    if i%6 == 4:
                        res5 += texte[indice]
                    if i%6 == 5:
                        res6 += texte[indice]     
    res = [res1,res2,res3,res4,res5,res6]              
    return res


# on obtient:
# premières lettres:'kismcteiwjznvdfivdrjnvtlwisjrehvjzyinjejhrizqsrnmiurmzve' 
# deuxièmes lettres: 'vagzronwehyodtjydklvzfefyfrxwucnrjubjldqctnrbhtndevjkocj'
# troisièmes lettres: 'qdqwvibolusrwsàevrevifiakvivzpasgiipezppemspzumztvrffue'
# quatrièmes lettres: 'swfrjrifMzqbvdbvijnzreyimjndozptryiktrfznimemziwjkydjsq'
# cinquièmes lettres: 'tqmnmtziipnerrvvstkjutsevyowjrttuibeppjdptttzptfasmjbfe'
# sixièmes lettres: 'ereoqcemwvvspfcjhhfxvesvscbvnwossuutrctwvrnzrvritqfuvnq'


#on fait une attaque statistique sur chacun de ces regroupements parcequ'ils sont tous chiffré par un décalage d'une meme lettre 
# et on essaye de connaitre chacune des 6 lettres du mot de passe L1, L2, L3, L4, L5, L6 en se servant aussi des lettres comme c' 
# et u' puisque on sait qu'elle correspondent soit à un l' soit à un d'. 

def frequence(message_chiffre):
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


#print (frequence(decoupe_texte(mirroir_message_chiffre)[0])) 
# [['k', 1.75], ['i', 12.28], ['s', 5.26], ['m', 5.26], ['c', 1.75], ['t', 3.51], ['e', 7.02], ['w', 3.51], ['j', 10.53], 
# ['z', 7.02], ['n', 7.02], ['v', 8.77], ['d', 3.51], ['f', 1.75], ['r', 8.77], ['l', 1.75], ['h', 3.51], ['y', 1.75], ['q', 1.75], ['u', 1.75]]

#print (frequence(decoupe_texte(mirroir_message_chiffre)[1])) 
#[['v', 5.26], ['a', 1.75], ['g', 1.75], ['z', 3.51], ['r', 7.02], ['o', 5.26], ['n', 7.02], ['w', 3.51], ['e', 5.26], ['h', 3.51], ['y', 5.26], 
# ['d', 7.02], ['t', 5.26], ['j', 8.77], ['k', 3.51], ['l', 3.51], ['f', 5.26], ['x', 1.75], ['u', 3.51], ['c', 5.26], ['b', 3.51], ['q', 1.75]]
# -> j est la plus fréquente et plusieurs fois en fin de mot donc correspond à un s donc l2 = r

#print (frequence(decoupe_texte(mirroir_message_chiffre)[2])) 
# [['q', 3.57], ['d', 1.79], ['w', 3.57], ['v', 10.71], ['i', 10.71], ['b', 1.79], ['o', 1.79], ['l', 1.79], ['u', 5.36], ['s', 7.14], ['r', 5.36], 
# ['e', 8.93], ['f', 5.36], ['a', 3.57], ['k', 1.79], ['z', 7.14], ['p', 8.93], ['g', 1.79], ['m', 3.57], ['t', 1.79]]
# -> i est la plus fréquente donc pourrais correspondre à un i donc l3 = a

#print (frequence(decoupe_texte(mirroir_message_chiffre)[3])) 
#[['s', 3.57], ['w', 3.57], ['f', 5.36], ['r', 8.93], ['j', 8.93], ['i', 10.71], ['z', 8.93], ['q', 3.57], ['b', 3.57], ['v', 3.57], ['d', 5.36], 
# ['n', 5.36], ['e', 3.57], ['y', 5.36], ['m', 5.36], ['o', 1.79], ['p', 1.79], ['t', 3.57], ['k', 3.57]]
# -> l4 = v

#print (frequence(decoupe_texte(mirroir_message_chiffre)[4])) 
#[['t', 17.86], ['q', 1.79], ['m', 5.36], ['n', 3.57], ['z', 3.57], ['i', 5.36], ['p', 8.93], ['e', 7.14], ['r', 5.36], ['v', 5.36], 
# ['s', 5.36], ['k', 1.79], ['j', 7.14], ['u', 3.57], ['y', 1.79], ['o', 1.79], ['w', 1.79], ['b', 3.57], ['d', 1.79], ['f', 3.57], ['a', 1.79]]
# -> l5 = e

#print (frequence(decoupe_texte(mirroir_message_chiffre)[5])) 
#[['e', 7.14], ['r', 8.93], ['o', 3.57], ['q', 5.36], ['c', 7.14], ['m', 1.79], ['w', 5.36], ['v', 14.29], ['s', 8.93], ['p', 1.79], ['f', 5.36], 
# ['j', 1.79], ['h', 3.57], ['x', 1.79], ['b', 1.79], ['n', 5.36], ['u', 5.36], ['t', 5.36], ['z', 1.79], ['i', 1.79]]

# après avoir supposer quatres des lettres du mot de passe, on obtient "rave", supposons que la clé était "braves" (comme dans l'indice), 
# on remarque que le message déchiffré fait presque du sens, on obtient d'ailleurs "je vobdrais pas", ce qui pourrais dire "je voudrais pas"
# on en déduit alors que le mot clé est "bravez"

#on utilise les fonctions du texte 3 pour déchiffrer le texte avec la clé retrouvée:

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

print("Le message déchiffré est:", dec_texte_inverse(mirroir_message_chiffre,"bravez"))

#Réponse:
#je voudrais pas crever avant d'avoir connu les chiens noirs du Mexique qui dorment sans rever les singes à cul nu devoreurs de tropiques les araignees d'argent au nid truffe de bulles  
# je voudrais pas crever sans savoir si la lune sous son faux air de thune a un cote pointu si le soleil est froid si les quatre saisons ne sont vraiment que quatre sans avoir essaye de porter une robe sur les grands boulevards
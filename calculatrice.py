#importation de biblioteque
import os

#verification des types de saisie
def is_number(d):
    try:
        float(d)
        return True
    except ValueError:
        return False

#verification du saisie des nombre
def nb_input():
    n = input("entrez un nombre : \n")
    while  not is_number(n):
        n = input("entrez un nombre : \n")
    n = float(n)
    return n

#verification du saisie de l'operateur
def op_input ():

    test_l = ["+", "-", "*", "/", "="]

    x = input ("donner l'operateur : \n")
    while not x in test_l:
        x = input ("donner l'operateur : \n")

    return x

#fonction de calcul
def calcul (l_hist):

    hist = open("historique.txt", "a")

    test = True

    test1 = True

    t = nb_input()

    while test :

        y = op_input()
        if y == "=":
            break
        
        z = nb_input()


        if (y == "/") and (z == 0):
            print ("la division par 0 est imposible")
            test1 = False
            break

        t_his = t

        if y == "+":
            t += z

        elif y == "-":
            t -= z

        elif y == "*":
            t *= z

        elif y == "/":
            t /= z

        list_for_hist = [str (element) for element in [t_his, y, z, "=", t]]
        str_for_hist = " ".join(list_for_hist) + "\n"
        hist.write (str_for_hist)

    if test1:
        print (t)
    hist.close()

#fonction de verification de contenue de fichier
def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

#fonctiond de supression d'une ligne de fichier
def del_hist (n_ligne):
    try:
        with open('historique.txt', 'r') as fr:
            lines = fr.readlines()
            
            ptr = 1
        
            with open('historique.txt', 'w') as fw:
                for line in lines:
                
                    if ptr != n_ligne:
                        fw.write(line)
                    ptr += 1
        
    except:
        print("Oops! erruer")

#foanction d'affichage du fichier historique.txt
def histoire ():
    nb_ligne = 1
    hist = open("historique.txt", "r")
    ligne = hist.readline()

    while ligne:
        print (nb_ligne, ":", ligne)

        ligne = hist.readline()
        nb_ligne += 1
    if not is_file_empty("historique.txt"):
        ef_test = input ("voulez vous effacer une ligne oui ou non : \n")
        while not (ef_test == "oui" or ef_test == "non"):
            ef_test = input ("voulez vous effacer une ligne oui ou non : \n")

    while ef_test == "oui" and not is_file_empty("historique.txt"):
        print ("donnez la ligne a effacer ", end ="")
        n_ligne = nb_input()
        
        del_hist(n_ligne)
        nb_ligne = 1
        hist = open("historique.txt", "r")
        ligne = hist.readline()

        while ligne:
            print (nb_ligne, ":", ligne)

            ligne = hist.readline()
            nb_ligne += 1
        if not is_file_empty("historique.txt"):
            ef_test = input ("voulez vous effacer une ligne oui ou non : \n")
            while not (ef_test == "oui" or ef_test == "non"):
                ef_test = input ("voulez vous effacer une ligne oui ou non : \n")



l_hist = []

chois = input ("vouler vous voire l'historique.txt oui ou non : \n")
while not (chois == "oui" or chois == "non"):
    chois = input ("vouler vous voire l'historique.txt oui ou non : \n")

if (chois == "oui"):
    try:
        histoire()
    except:
        print ("le fichier nexiste pas ou il est vide")
        calcul (l_hist)
else:
    calcul (l_hist)

from new_user import *
from cheek_user import *
from add_argent import *
from get_total_of_user import *
from get_history import *
from delet_user import *
import time

while True:
    total = 0
    montant = 0
    user = ""

    ftre = 1


    def login():
        global ftre
        global user
        while ftre == 1:
            cam1 = int(input("1-- creer un  compte. \n2--se connecter a un compte.\n"))

            if cam1 == 1:
                user = str(input("entrez un nom pour votre compte : "))
                pw = str(input("entrer votre mot de passe : "))
                cam2 = int(input("1-- confermer. \n2--retour. \n"))
                if cam2 == 1:
                    add_user(user, pw)
                    print("vorte compte est creer avec seccee")
                else:
                    print("retour...")
            elif cam1 == 2:
                user = str(input("nom de votre compte : "))
                pw = str(input("votre mot de passe : "))
                if check_user(user, pw) == "TT":
                    print("verrification...")
                    time.sleep(3)
                    print("vous etes connectee à votre compte : " + user)
                    ftre = 2
                if check_user(user, pw) == "TF":
                    print("password incorrecte")
                if check_user(user, pw) == "FT":
                    print("user n'existe pas")
                if check_user(user, pw) == "FF":
                    print("votre informations incorrecte")


            else:
                print("commande n'existe pas ?! ")


    login()

    while ftre == 2:
        cam3 = int(input(
            "\n1--verser de l'argent. \n2--Retirer de l'argent. \n3--voir total d'argent.\n4--votre historique sur le "
            "compte. \n5--supprimer votre compte.\n6--deconnecter de votre compte.\n"))
        if cam3 == 1:
            montant = int(input("combien de Dirham voulez vous verser dans votre compte: "))
            if add_to_total(user, montant):
                print("vous avez verser " + str(montant) + " DH avec seccee  sur votre compte.")
            else:
                print("pardon un erors s'est passe.")

        # ============retirer d'argent de compte=============
        elif cam3 == 2:
            montant = int(input("combien de Dirham voulez vous retirez de votre compte: "))
            if add_to_total(user, -montant):
                print("vous avez retirer " + str(montant) + " DH avec seccee  sur votre compte.")
            else:
                print("pardon un erors s'est passe.")
        elif cam3 == 3:
            print("votre total d'argent dans votre compte est de : " + str(get_user_total(user)) + "DH.")
        elif cam3 == 4:
            print("voici votre historique de compte : \n" + get_historique_user(user))
        elif cam3 == 5:
            confir = int(input("1--confirmer le supprime de compte: " + user + ".\n2--retour...\n"))
            if confir == 1:
                delete_user(user)
                print("votre compte est supprime")
            else:
                print("retour...")
        elif cam3 == 6:
            print("Retour au menu pricipale...")
            ftre = 1
        else:
            print("commande n'existe pas ?! ")

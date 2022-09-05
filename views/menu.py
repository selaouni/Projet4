#from controllers import (player_controller, tournoi_controller)
import json
#from controllers import tournoi_controller


class FirstTitles:

    def titles(self):
        print("-------------------- Bienvenue - Tournoi d'échecs --------------------")
        print("-" * 70)
        print("-" * 70)
        print("----------------------- Menu principal ---------------------------------")
        print("-" * 70)


class Menu:
    main_menu = [("1", "Créer un nouveau joueur"),
                ("2", "Mettre à jour un joueur"),
                ("3", "Créer un nouveau tournoi"),
                ("4", "Reprendre un tournoi"),
                ("5", "Rapport joueurs"),
                ("6", "Rapport tournoi"),
                ("7", "Quitter")]



    report_menu = [("1",  "Afficher les tournois"),
                   ("2", "Afficher les joueurs par ordre alphabétique"),
                   ("3", "Afficher les tours"),
                   ("4", "Afficher les matchs"),
                   ("5", "Afficher les joueurs selon leurs classements"),]

    def __call__(self, menu):
        for i in menu:
            print(" - " + i[0] + " - " + i[1])
        while True:
            data = input("Saisir le chiffre correspondant au menu souhaité : ")
            for line in menu:
                if data == line[0]:
                    return str(line[0])
            print("Erreur ! Merci de saisir l'un des chiffres affichés")

class Menu_tournoi:

    # def __init__(self):
    #
    #     self.createTournoiController = tournoi_controller.CreateTournoiController()

    def add_player_menu(self):

        print("merci de choisir l'id'de joueurs à ajouter au tournoi")
        player1 = input("joueur N°1 : ")
        player2 = input("joueur N°2 : ")
        player3 = input("joueur N°3 : ")
        player4 = input("joueur N°4 : ")
        player5 = input("joueur N°5 : ")
        player6 = input("joueur N°6 : ")
        player7 = input("joueur N°7 : ")
        player8 = input("joueur N°8 : ")
        print("------- Les joueurs que vous avez choisi sont")

        NBR_PLAYER = 8
        player_list = []
        for i in range(NBR_PLAYER):
            player_list.append(int(locals()["player" + str(i + 1)]))
        return player_list


    # def __call__(self):










        # print("Message info: Joueur ajouté au tournoi")
        #
        # print("--------------------------------------- TOURNOI DEMARRE --------------------------------------")
        # print(
        #     "Merci de saisir les scores de ce tour : 1 point pour le gagnant, 0 point pour le perdant et 0.5 pour chaque joueur en cas de match nul ")
        # print("--- Score 1er match : ")
        # player1_score = input("score 1er joueur : ")
        # player2_score = input("score 2eme joueur : ")
        # print("--- Score 2eme match : ")
        # player3_score = input("score 1er joueur : ")
        # player4_score = input("score 2eme joueur : ")
        # print("--- Score 3eme match : ")
        # player5_score = input("score 1er joueur : ")
        # player6_score = input("score 2eme joueur")
        # print("--- Score 4eme match : ")
        # player7_score = input("score 1er joueur : ")
        # player8_score = input("score 2eme joueur")







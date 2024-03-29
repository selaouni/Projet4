from controllers import player_controller
from controllers import tournoi_controller

NBR_PLAYER = 8


class First_titles:

    # En-tete principal
    def titles(self):
        print("-------------------- Bienvenue - Tournoi d'échecs --------------------")
        print("-" * 70)
        print("-" * 70)
        print("----------------------- Menu principal ---------------------------------")
        print("-" * 70)


class Menu:
    # Menu principal affiché au tout debut de l'execution
    main_menu = [("1", "Créer un nouveau joueur"),
                 ("2", "Mettre à jour un joueur"),
                 ("3", "Créer un nouveau tournoi"),
                 ("4", "Reprendre un tournoi"),
                 ("5", "Rapport joueurs"),
                 ("6", "Rapport tournoi"),
                 ("7", "Quitter")]

    def __call__(self, menu):
        for i in menu:
            print(" - " + i[0] + " - " + i[1])
        while True:
            data = input("Merci de saisir le chiffre correspondant au menu souhaité : ")
            for line in menu:
                if data == line[0]:
                    return str(line[0])

            print("Erreur : Merci de saisir l'un des chiffres affichés")
            break


class Menu_tournoi:
    # Menu permet de renseigner les ids des joueurs à selectionnés pour un tournoi
    def add_player_menu(self):

        print("Merci de choisir l'id'de joueurs à ajouter au tournoi")
        player1 = input("joueur N°1 : ")
        player2 = input("joueur N°2 : ")
        player3 = input("joueur N°3 : ")
        player4 = input("joueur N°4 : ")
        player5 = input("joueur N°5 : ")
        player6 = input("joueur N°6 : ")
        player7 = input("joueur N°7 : ")
        player8 = input("joueur N°8 : ")
        print("**** Les joueurs que vous avez choisi sont :  ")
        player_list = []
        for i in range(NBR_PLAYER):
            player_list.append(int(locals()["player" + str(i + 1)]))
        return player_list

    def menu_add_score(self):
        # affiché au moment de la saisie des scores d'un tour

        print("--------------------------------------- TOURNOI DEMARRE --------------------------------------")
        print("Merci de saisir les scores de chaque tour: ")
        print("-- 1 point pour le gagnant -- 0 point pour le pérdant -- 0.5 pour chaque joueur en cas de match nul --")

    def time_control_menu(self):
        time_control_input = input("Merci de choisir le contrôle du temps -- Bullet, Blits ou Coup rapide : ")
        return time_control_input


class Player_report:
    def __init__(self):
        self.player = player_controller.CreatePlayerController()
    # Affiche les rapports player
    def __call__(self):
       self.player.player_report()


class Tournoi_report:

    # Affiche les rapports du tournoi
    def __init__(self):
        self.tournoi = tournoi_controller.CreateTournoiController()

    def __call__(self):
        self.tournoi.tournoi_report()





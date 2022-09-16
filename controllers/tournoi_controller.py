from views import menu
from controllers import base_controller
from controllers import player_controller
from models import tournois
from models import player
from models import match
from models import tour

from datetime import datetime
from tinydb import Query
import json
import pandas as pd


class CreateTournoiController:

    def __init__(self):
        self.menu_display = menu.Menu()
        self.player = player.Player()
        self.tournoi_value = []
        self.tournoi_display = menu.Menu_tournoi()
        self.player_controller = player_controller.CreatePlayerController()
        #self.tournoi_players = []
        #self.main_controller_menu = base_controller.MainMenuController()
        self.tournoi = tournois.Tournoi()
        self.run_tournoi = Run_tournoi()
        self.players_id = []


    def __call__(self):

        self.tournoi_object = tournois.Tournoi()
        self.tournoi_value.append(self.add_name())
        self.tournoi_value.append(self.add_Place())
        self.tournoi_value.append(self.add_tournoi_date())
        self.tournoi_value.append(self.number_of_tours())
        self.tournoi_value.append(self.players_id)
        self.add_players()
        self.tournoi_value.append(self.add_timing())
        self.tournoi_value.append(self.add_description())
        self.tournoi_display.menu_add_score()
        self.tournoi_object = tournois.Tournoi(self.tournoi_value[0], self.tournoi_value[1], self.
                                               tournoi_value[2], self.tournoi_value[3], self.tournoi_value[4],
                                               self.tournoi_value[5], self.tournoi_value[6])
        self.run_tournoi.run_first_tour(self.tournoi_object)
        self.tournoi_value.append(self.tournoi.tour_list)
        self.run_tournoi.run_other_tours(self.tournoi_object)
        self.tournoi_object.save_tournoi(self.tournoi_value)
        print("Message info ----> Tournoi sauvegardé dans la base de donnée")
        print("*" * 140)

    def add_name(self):
        valid_name = False
        while not valid_name:
            tournoi_name = input("Saisir le nom du tournoi - exemple -> Tournoi1: ")
            if tournoi_name != "":
                valid_name = True
            else:
                print("Erreur: merci de saisir un nom valid")
        return tournoi_name

    def add_Place(self):
        valid_place = False
        while not valid_place:
            place = input("saisir l'endroit du tournoi: ")
            if place != "" and place.isalpha():
                valid_place = True
            else:
                print("Erreur: Merci de saisir une localisation correcte")
        return place

    def add_tournoi_date(self):
        date_list = []
        print("-------------- Debut saisie de la date du tournoi----------------")
        valid_day = False
        while not valid_day:

            self.birth_day = input("saisir le jour du tournoi: ")
            if int(self.birth_day) < 32 and len(self.birth_day) == 2 \
                    and self.birth_day != "00" and self.birth_day.isdigit():
                valid_day = True
                date_list.append(self.birth_day)
            else:
                print("Erreur: Merci de saisir un nombre à 2 chiffres inférieur à 31")

        valid_month = False
        while not valid_month:
            self.birth_month = input("saisir le mois du tournoi:")
            if int(self.birth_month) < 13 and len(self.birth_month) == 2 \
                    and self.birth_month != "00" and self.birth_month.isdigit():
                valid_month = True
                date_list.append(self.birth_month)
            else:
                print("Erreur: Merci de saisir un nombre valide, à 2 chiffres et inférieur à 12")

        valid_year = False
        while not valid_year:
            self.birth_year = input("saisir l'année du tournoi: ")
            if len(self.birth_year) == 4 and self.birth_year != "0000" and self.birth_year.isdigit():
                valid_year = True
                date_list.append(self.birth_year)
            else:
                print("Erreur: Merci de saisir une année à 4 chiffres ")

        print("-------------- Fin saisie de la date du tournoi ----------------")

        return f"{date_list[0]}/{date_list[1]}/{date_list[2]}"

    def number_of_tours(self):
        tour_nbr = 4
        return tour_nbr

    def add_timing(self):
        self.tournoi.timing = self.tournoi_display.time_control_menu()
        return self.tournoi.timing

    def add_description(self):
        description = input("Saisir la description du tournoi : ")
        return description

    def add_players(self):
        """
        :return: liste des match divisée en deux
        Cette fonction permet de recuprer les id des joueurs saisis, cherche les info associées à ce joueur dans
        la BD et fait le tri par classement puis divise la liste en deux. Le return de cette fonction permet de
        constituer les matchs par la suite
        """
        players_id = self.tournoi_display.add_player_menu()
        self.players_id.append(players_id)
        print("Liste des id : ", players_id)
        sorted_player = self.run_tournoi.sorted_first_time(self.player_controller.get_info_by_id(players_id))
        file = open('DB_players.json')
        json.load(file)
        self.player.db_player.update({'Score': 0.0})
        self.player.db_player.update({'Score': 0.0})

        for i in sorted_player:
            print(i)

        list(sorted_player).clear()
        splitted_players = self.run_tournoi.split(list(sorted_player))

        match_list = self.run_tournoi.make_match(splitted_players[0], splitted_players[1])
        self.tournoi.player_list = match_list
        print("Message info ----> Message info: Les Joueurs sont ajoutés")
        return self.tournoi.player_list
    def tournoi_report(self):
        print("-" * 80)
        print(" --------------------------- Rapport tournoi ---------------------------------- ")
        print("-" * 80)
        print("A - Liste de tous les tournois :")
        self.tournoi = tournois.Tournoi()
        tournoi_info = self.tournoi.db_tournoi.all()
        for i in tournoi_info:
            tournoi_unserialized = self.tournoi.unserialized(i)
            print(
                f" {tournoi_unserialized.name} - {tournoi_unserialized.place} "
                f" - {tournoi_unserialized.date}"
                f" - {tournoi_unserialized.timing} - Description: {tournoi_unserialized.description} ")
        print("-" * 80)
        print("B - Liste de tous les tour d'un tournoi :")
        for i in tournoi_info:
            tournoi_unserialized = self.tournoi.unserialized(i)
            print(
                f" {tournoi_unserialized.name} - {tournoi_unserialized.tour_list} - {tournoi_unserialized.place} "
                f" - {tournoi_unserialized.date}")

        print("-" * 80)
        print("C - Liste de tous les matchs d'un tournoi :")
        tournoi_unserialized = []
        for i in tournoi_info:
            tournoi_unserialized = self.tournoi.unserialized(i)
            print(
                f" {tournoi_unserialized.name} - {tournoi_unserialized.tour_list}")

        print("-" * 80)

class Run_tour:
    def __init__(self):
        self.match = match.Matchs
        self.tour = tour.Tours
        self.player = player.Player()
        self.player1 = player.Player()
        self.player2 = player.Player()
        self.player_value = []
        self.tour_serialized = []
    def run(self, match_list, tournoi_object):
        """
        :param la liste des joueurs pour un tournoi, l'instance tournoi
        :return: le tour sérialisé contenant les infos sur le nom du match, la liste des matchs joués
        et le timing du tour.
        Cette fonction permet de lancer un tour, crée donc l'objet match qui en decoule et sauvegarde les scores des
        joueurs dans la base de données "DB_players.json"
        """

        self.Date_Time_Start = datetime.now()
        print("Tour lancé à : ", self.Date_Time_Start)
        self.tour_name = "Tour " + str(len(tournoi_object.tour_list) + 1)
        self.list_tour = []
        self.match_list = []
        while len(match_list) > 0:
            # création de l'objet match
            match = self.match(self.tour_name, match_list[0], match_list[1])
            self.player1.unserialized(match_list[0])
            self.player2.unserialized(match_list[1])
            self.list_tour.append(match)
            del match_list[0:2]
        print("----- Début saisie ", self.tour_name, "------")
        count = 0
        for match in self.list_tour:
            count += 1
            print("Match --> ", count)
            score_player1 = float(input("Score du premier joueur  : "))
            match.score_player1 = score_player1
            self.player1.score = score_player1
            score_player2 = input("Score du deuxiem joueur : ")
            match.score_player2 = float(score_player2)
            self.player2.score = float(score_player2)
            self.match_list.append(([match.player1['id'],
                                     match.score_player1],
                                    [match.player2['id'],
                                     match.score_player2]))
            print("Résultats pris en compte : ", self.match_list)
            query = Query()
            self.player.db_player.update({'Score': match.score_player1}, query.id == match.player1['id'])
            self.player.db_player.update({'Score': match.score_player2}, query.id == match.player2['id'])
        self.Date_Time_End = datetime.now()
        print("Tour terminé à : ", self.Date_Time_End)
        tour_object = self.tour(self.tour_name, self.match_list, str(self.Date_Time_Start), str(self.Date_Time_End))

        self.tour_serialized.append(tour_object.serialize())

        return self.tour_serialized


class Run_tournoi:
    def __init__(self):
        self.player = player.Player()
        self.match = match.Matchs()
        self.tour = tour.Tours()
        self.tournoi_display = menu.Menu_tournoi()
        self.player = player.Player()
        self.tournoi_value = []
        self.tournoi_players = []
        self.main_controller_menu = base_controller.MainMenuController()
        self.tournoi = tournois.Tournoi()
        self.player_controller= player_controller.CreatePlayerController()
        self.run_tour= Run_tour()


    def add_matchs(self):
        self.tournoi.tour_list = self.run_first_tour()
        return self.tournoi.tour_list
    def sorted_first_time(self, list_player_to_sort):
        """
        :param:  liste avec les informations associées à un joueurs
        :return: Liste triée par classement
        Cette fonction concerne le premier tour
        """
        player_list = pd.DataFrame(list_player_to_sort)
        player_list = player_list.sort_values(("Classement"), ascending=False)
        self.player_list = player_list.T.to_dict().values()
        return(self.player_list)

    def split(self, sorted_player_to_split):
        """
        :param:  Liste joueurs triée par classement
        :return: Liste joueurs divisée en deux listes
        Cette fonction concerne le premier tour
        """
        half = len(sorted_player_to_split) // 2
        player_splitted = sorted_player_to_split[:half], sorted_player_to_split[half:]
        return player_splitted

    def make_match(self, players_list1, players_list2):
        """
        :param:  Liste joueurs triée et divisée en deux listes
        :return: List des pairs du match
        """
        file = open('DB_players.json')
        json.load(file)
        players_match = []
        for i in range(len(self.player_list) // 2):
            players_match.append(players_list1[i])
            players_match.append(players_list2[i])
        self.player_list = players_match
        print("-" * 140)
        print("**** Génaréation des pairs : ")
        for i in range(0, (self.tournoi.nbr_tours * 2), 2):
            print("Joueurs match", i + 1, " ----> :", players_match[i], players_match[i + 1])
            print("-" * 140)
        return self.player_list

    def sorted_second_time(self, tour_list):
        """
        :param:  Liste joueurs du tournoi
        :return: List joueurs triés par score puis par classement si égalité au niveau du score
        Cette fonction s'applique à partir du 2eme tour
        """
        print ("test tour_list", tour_list)
        players = []
        players_id = []
        tour_object = []
        for i in range(len(tour_list)):
            tour_object = self.tour.unserialize(tour_list)

        for m in tour_object.match_list:
            for p in m:
                players.append(p)

        for p in players:
            players_id.append(p[0])

        info_player = self.player_controller.get_info_by_id(players_id)
        player_list = pd.DataFrame(info_player)
        player_list = player_list.sort_values(by=['Score', 'Classement'], ascending=False)
        players_by_score = player_list.T.to_dict().values()
        return players_by_score

    def run_first_tour(self, tournoi_object):
        """
        Cette fonction permet de lancer le premier tour en se basant sur une liste de joueurs  triée par classement
        """
        self.tour_list = self.run_tour.run(self.player_list, tournoi_object)
        return self.tour_list

    def run_other_tours(self, tournoi_object):
        """
        Cette fonction permet de lancer le 2eme, 3eme et 4eme tour en se basant sur une liste de joueurs
        triée  cette fois ci par score
        """
        sorted_players = []
        for i in range(self.tournoi.nbr_tours - 1):
            file = open('DB_players.json')
            json.load(file)
            del sorted_players
            sorted_players = self.sorted_second_time(self.tour_list[i])
            print("test self.sorted_players 2", sorted_players)
            print("*" * 140)
            launched_tour = self.run_tour.run(list(sorted_players), tournoi_object)
            tournoi_object.tour_list = launched_tour




        print("*" * 140)
        print("-------------------------------------------  TOURNOI TERMINE ----------------------------------------")
        print("*" * 140)

class ReLoadTournament:
    def __init__(self):
        self.tournoi =tournois.Tournoi()
    def __call__(self):

        tournaments_reloaded = False
        print("------------------------ Reprendre un tournoi ------------------------\n")
        for tournoi in self.tournoi.db_tournoi:
            if tournoi["liste des Tours"] != []:
                if len(tournoi["liste des Tours"]) < int(tournoi["Numbre of tours"]):
                    print(f" {tournament['nom du tournoi']} {tournament['place']}")
                    tournaments_reloaded = True

        return tournaments_reloaded

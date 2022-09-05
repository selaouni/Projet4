
#from views import menu
from models import tournoi
from models import player
from controllers import base_controller
from views import menu
import json
from tinydb import Query


class CreateTournoiController:

    def __init__(self):
        self.menu_display = menu.Menu()
        self.tournoi_display = menu.Menu_tournoi()
        #self.menu_tournoi = menu.Menu_tournoi()
        self.player = player.Player()
        self.tournoi_value = []
        self.tournoi_players = []
        self.main_controller_menu = base_controller.MainMenuController()
        self.tournoi = tournoi.Tournoi()
        self.players_serialized = []



    def add_name(self):
        valid_name = False
        while not valid_name:
            tournoi_name = input("Saisir le nom du tournoi - exemple -> Round1: ")
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
        print("--------------Debut de la saisie de la date du tournoi----------------")
        valid_day = False
        while not valid_day:

            self.birth_day = input("saisir le jour du tournoi: ")
            if  int(self.birth_day) < 32 and len(self.birth_day) == 2 and self.birth_day != "00" and self.birth_day.isdigit():
                valid_day = True
                date_list.append(self.birth_day)
            else:
                print("Erreur: Merci de saisir un nombre à 2 chiffres inférieur à 31")

        valid_month = False
        while not valid_month:
            self.birth_month = input("saisir le mois du tournoi:")
            if int(self.birth_month) < 13 and len(self.birth_month) == 2 and self.birth_month != "00" and self.birth_month.isdigit():
                valid_month = True
                date_list.append(self.birth_month)
            else:
                print("Erreur: Merci de saisir un nombre valide, à 2 chiffres et inférieur à 12")

        valid_year = False
        while not valid_year:
            self.birth_year = input("saisir l'année du tournoi: ")
            if len(self.birth_year) == 4 and  self.birth_year != "0000" and self.birth_year.isdigit():
                valid_year = True
                date_list.append(self.birth_year)
            else:
                print("Erreur: Merci de saisir une année à 4 chiffres ")

        return f"{date_list[0]}/{date_list[1]}/{date_list[2]}"

    def number_of_tours(self):
        number_tours = 4
        return number_tours
    def add_timing(self):
        pass

    def add_description(self):
        description = input("Saisir la description du tournoi : ")
        return description

    # def add_players(self, player_id):
    #     self.tournoi_players.append(player_id)
    #     return (self.tournoi_players)
    def get_info_by_id(self, list_player_id):

        query = Query()
        for i in range(len(list_player_id)):
            current_players = self.player.db_player.get(query.id == list_player_id[i])
            self.players_serialized.append(current_players)
            print("test current player", current_players)
        return (self.players_serialized)

    def add_players(self):
        player_id = self.tournoi_display.add_player_menu()
        sorted_player = self.tournoi.sorted_first_time(self.get_info_by_id(player_id))
        for i in sorted_player:
            print(i)
        player_id.clear()
        self.tournoi.split(list(sorted_player))


    #     Show_players =
    #
    #     db_player.read_json('DB_players.json')
    #
    #     print(Show_players)




        #  with open('DB_players.json') as player_data:
        # player_data = 'DB_players.json'
        # data = json.loads(open(player_data).read())
        # data = json.load(player_data)
        # for i in data:
        #     try:
        #         result = i[id]["rank"]
        #         return (result)
        #     except KeyError:
        #         print("cet id n'existe pas dans la base de donnée")
        #
        #     if i['id'] == str(id):
        #         result = i["rank"]




    def __call__(self):
        self.tournoi_model = tournoi.Tournoi()
        self.tournoi_value.append(self.add_name())
        self.tournoi_value.append(self.add_Place())
        self.tournoi_value.append(self.add_tournoi_date())
        self.tournoi_value.append(self.number_of_tours())
        self.add_players()

        # print("---------------- Affichage des joueurs ----------------")
        # # with open('DB_players.json') as player_data:
        # #     data = json.load(player_data)
        # #     print(json.dumps(data, sort_keys=True, indent=4))
        #
        # print("merci de choisir l'id'de joueurs à ajouter au tournoi")
        #
        # player1 = input("joueur N°1 : ")
        # player2 = input("joueur N°2 : ")
        # player3 = input("joueur N°3 : ")
        # player4 = input("joueur N°4 : ")
        # player5 = input("joueur N°5 : ")
        # player6 = input("joueur N°6 : ")
        # player7 = input("joueur N°7 : ")
        # player8 = input("joueur N°8 : ")
        # print("------- Les joueurs que vous avez choisi sont")

        # NBR_PLAYER = 8
        # player_list = []
        # for i in range(NBR_PLAYER):
        #     player_list = self.add_players(int(locals()["player" + str(i+1)]))
        #
        # #print("test player_list : ", player_list)
        # sorted_player = []
        # sorted_player = self.tournoi.sorted_first_time(self.get_info_by_id(player_list))
        # for i in sorted_player:
        #     print(i)
        #
        # player_list.clear()
        #
        # self.tournoi.split(list(sorted_player))














        #self.tournoi.run_tournoi()

        # NBR_PLAYER = 8
        # for i in range(NBR_PLAYER):
        #     result = [x for x in player_data if x[int("id")] == locals()["player" + str(i+1)]]
        #     self.add_players(result)

        # Reconvertir l'instance serialisée de la table player (json) en une instance class player

        print("Message info: Joueur ajouté au tournoi")

        #print("--------------------------------------- TOURNOI DEMARRE --------------------------------------")
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

        self.tournoi_value.append(self.tournoi_players)

        self.tournoi_value.append(self.add_timing())
        self.tournoi_value.append(self.add_description())
        self.tournoi_model.save_tournoi(self.tournoi_value)
        print("Message info: Tournoi sauvegardé dans la base de donnée")
        #self.tournoi_model.show_all()
        self.main_controller_menu()



class TournoiReport:


    def __call__(self):
        print(" --------------------------- Rapport tournoi --------------------------- ")





'''
class Controller:

    def __init__(self, Tournoi, Player, view):

        # models
        self.Tournoi: List[Tournoi] = []
        self.Player: List[Player] = []

        # views
        self.view = view

    def start_game(self):
        pass
    def Sort(player):
        pass
    def add_player(self, player):
        pass

'''
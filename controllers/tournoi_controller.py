
#from views import menu
from models import tournoi
from models import player
from controllers import base_controller


class CreateTournoiController:

    def __init__(self):
        self.menu_display = menu.Menu()
        self.player = player.Player()
        self.tournoi_value = []
        self.tournoi_players = []
        self.main_controller_menu = base_controller.MainMenuController()
        self.tournoi = tournoi.Tournoi()

    def add_name(self):
        valid_name = False
        while not valid_name:
            tournoi_name = input("Saisir le nom du tournoi - exemple : Round1")
            if tournoi_name != "" and tournoi_name.isalpha():
                valid_name = True
            else:
                print("Erreur: merci de saisir un nom")
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
        print("-------Debut de la saisie de la date du tournoi-------")
        valid_day = False
        while not valid_day:

            self.birth_day = input("saisir le jour du tournoi: ")
            if  int(self.birth_day) < 32 and len(self.birth_day) == 2 and self.birth_day.isdigit():
                valid_day = True
                date_list.append(self.birth_day)
            else:
                print("Erreur: Merci de saisir un nombre à 2 chiffres inférieur à 31")

        valid_month = False
        while not valid_month:
            self.birth_month = input("saisir le mois du tournoi:")
            if  int(self.birth_month) < 13 and len(self.birth_month) == 2 and self.birth_month.isdigit():
                valid_month = True
                date_list.append(self.birth_month)
            else:
                print("Erreur: Merci de saisir un nombre à 2 chiffres inférieur à 12")

        valid_year = False
        while not valid_year:
            self.birth_year = input("saisir l'année du tournoi: ")
            if  len(self.birth_year) == 4 and self.birth_year.isdigit():
                valid_year = True
                date_list.append(self.birth_year)
            else:
                print("Erreur: Merci de saisir une année à 4 chiffres ")

        return f"{date_list[0]}/{date_list[1]}/{date_list[2]}"

    def number_of_tours(self):
        number_tours = 4
        return number_tours
    def add_timing(self)
        pass

    def add_description(self):
        description = input("Saisir la description du tournoi : ")

        return description



    def add_players_to_tournoi(self):

       pass

    def __call__(self):
        self.tournoi_value.append(self.add_name())
        self.tournoi_value.append(self.add_Place())
        self.tournoi_value.append(self.add_tournoi_date())
        self.tournoi_value.append(self.number_of_tours())
        self.tournoi_value.append(self.add_timing())
        self.tournoi_value.append(self.add_description())
        self.add_players_to_tournoi()
        self.tournoi_value.append(self.tournoi_players)
        self.main_controller_menu()


class Tournoi_run:
    pass

class TournoiReport:
    pass




"""

tournoi_object = CreateTournoiController()
tournoi_place= CreateTournoiController.add_Place(self=tournoi_object)
tournoi_date = CreateTournoiController.add_tournoi_date(self=tournoi_object)
#tournoi_number_of_rounds = CreateTournoiController.add_number_of_rounds(self=tournoi_object)
tournoi_date_description = CreateTournoiController.add_description(self=tournoi_object)
tournoi_players_Tournoi= CreateTournoiController.add_players_Tournoi(self=tournoi_object)
print(tournoi_place)
print(tournoi_date)
#print(tournoi_number_of_rounds)
print(tournoi_date_description)
print(tournoi_players_Tournoi)






"""















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
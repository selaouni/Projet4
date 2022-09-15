from models import tournois
from models import player
from views import menu
from controllers import base_controller


class CreateTournoiController:

    def __init__(self):
        self.menu_display = menu.Menu()
        self.tournoi_display = menu.Menu_tournoi()
        self.player = player.Player()
        self.tournoi_value = []
        self.tournoi_players = []
        self.main_controller_menu = base_controller.MainMenuController()
        self.tournoi = tournois.Tournoi()
        self.players_id = []
        self.players_id = []

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
        print("--------------Debut de la saisie de la date du tournoi----------------")
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

        return f"{date_list[0]}/{date_list[1]}/{date_list[2]}"

    def number_of_tours(self):
        number_tours = 4
        return number_tours

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
        print("Liste des id : ", self.tournoi.player_list)

        sorted_player = self.tournoi.sorted_first_time(self.tournoi.get_info_by_id(players_id))
        for i in sorted_player:
            print(i)

        list(sorted_player).clear()
        splitted_players = self.tournoi.split(list(sorted_player))

        match_list = self.tournoi.make_match(splitted_players[0], splitted_players[1])
        self.tournoi.player_list = match_list
        print("Message info: Les Joueurs sont ajoutés")
        return self.tournoi.player_list

    def add_matchs(self):
        self.tournoi.tour_list = self.tournoi.run_first_tour()
        return self.tournoi.tour_list

    def __call__(self):

        self.tournoi_model = tournois.Tournoi()
        self.tournoi_value.append(self.add_name())
        self.tournoi_value.append(self.add_Place())
        self.tournoi_value.append(self.add_tournoi_date())
        self.tournoi_value.append(self.number_of_tours())
        self.tournoi_value.append(self.players_id)
        self.add_players()
        # self.player.initialize_score()
        self.tournoi_value.append(self.add_timing())
        self.tournoi_value.append(self.add_description())
        self.tournoi_display.menu_add_score()
        self.tournoi_model = tournois.Tournoi(self.tournoi_value[0], self.tournoi_value[1], self.
                                              tournoi_value[2], self.tournoi_value[3], self.tournoi_value[4],
                                              self.tournoi_value[5], self.tournoi_value[6])
        self.tournoi.run_first_tour(self.tournoi_model)
        self.tournoi_value.append(self.tournoi.tour_list)
        self.tournoi.run_other_tours(self.tournoi_model)
        self.tournoi_model.save_tournoi(self.tournoi_value)
        print("Message info ----> Tournoi sauvegardé dans la base de donnée")
        self.main_controller_menu()

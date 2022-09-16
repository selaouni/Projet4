from models import player
from models import tournois
from controllers import base_controller

from tinydb import Query

class CreatePlayerController:
    def __init__(self):
        self.player_value = []
        self.main_controller_menu = base_controller.MainMenuController()
        self.player = player.Player()
        self.tournoi = tournois.Tournoi()
        self.players_extracted = []

    def __call__(self):
        self.player_model = player.Player()
        self.player_value.append(self.add_id())
        self.player_value.append(self.add_first_name())
        self.player_value.append(self.add_last_name())
        self.player_value.append(self.add_birth_date())
        self.player_value.append(self.add_gender())
        self.player_value.append(self.add_rank())
        self.player_value.append(self.add_score())
        self.player_model.save_player(self.player_value)
        print("------> Message info: joueur sauvegardé dans la base de donnée")
        self.main_controller_menu()


    def add_id(self):
        valid_id = False
        while not valid_id:

            id = input("Entrez l'id du joueur': ")
            if id != "" and id.isdigit():
                valid_id = True
            else:
                print("Erreur: merci de saisir un id valide")
        return id

    def add_last_name(self):
        valid_last_name = False
        while not valid_last_name:

            last_name = input("Entrez le nom du joueur: ")
            if last_name != "" and last_name.isalpha():
                valid_last_name = True
            else:
                print("Erreur: merci de saisir un prénom valide")
        return last_name

    def add_first_name(self):
        valid_first_name = False
        while not valid_first_name:
            first_name = input("Entrez le prénom du joueur: ")
            if first_name != "" and first_name.isalpha():
                valid_first_name = True
            else:
                print("Erreur: merci de saisir un prénom valide ")
        return first_name

    def add_birth_date(self):
        birthdate_list = []
        print("-------------Debut de la saisie de la date---------------")
        valid_day = False
        while not valid_day:
            self.birth_day = input("Entrez le jour de naissance du joueur: ")
            if len(self.birth_day) == 2 and int(self.birth_day) < 32 and self.birth_day != "00" \
                    and self.birth_day.isdigit():
                valid_day = True
                birthdate_list.append(self.birth_day)
            else:
                print("Erreur: Merci de saisir un jour de naissance valide en 2 chiffres")

        valid_month = False
        while not valid_month:
            self.birth_month = input("Entrez le mois de naissance En chiffre: ")
            if len(self.birth_month) == 2 and int(self.birth_month) < 13 and self.birth_month != "00" \
                    and self.birth_month.isdigit():
                valid_month = True
                birthdate_list.append(self.birth_month)
            else:
                print("Erreur: Merci de saisir un nombre à 2 chiffres <= 12")

        valid_year = False
        while not valid_year:
            self.birth_year = input("Entrez l'année de naissance du joueur: ")
            if len(self.birth_year) == 4 and int(self.birth_year) < 2023 and self.birth_year != "0000" \
                    and self.birth_year.isdigit():
                valid_year = True
                birthdate_list.append(self.birth_year)
            else:
                print("Erreur: Merci de saisir une année de naissance valide en 4 chiffres")

        return f"{birthdate_list[0]}/{birthdate_list[1]}/{birthdate_list[2]}"

    def add_gender(self):
        valid_gender = False
        validated_gender = None
        while not valid_gender:
            gender = input("Saisir le genre du joueur 'Homme' ou 'Femme' : ")

            if gender == "Homme":
                valid_gender = True
                validated_gender = "Homme"
            elif gender == "Femme":
                valid_gender = True
                validated_gender = "Femme"
            else:
                print("Erreur: Merci de saisir un genre valide 'Homme' ou 'Femme'")
        return validated_gender

    def add_rank(self):
        valid_rank = False
        while not valid_rank:

            rank_player = input("Entrez le classement du joueur': ")
            if rank_player != "" and rank_player.isdigit() and int(rank_player) > 0:
                valid_rank = True
            else:
                print("Erreur: merci de saisir un chiffre positif")
        return rank_player

    def add_score(self):
        default_score = 0
        return default_score

    def get_info_by_id(self, list_player_id):
        """
        :param: Liste  des id saisis par l'utilisateur
        :return: une liste avec les informations associées à chaque id
        Cette fonction permet récuprer de la base de donnée "DB_players.json" toutes les informations
        d'un joueurs à partir de l'id donné
        """

        query = Query()
        for i in range(len(list_player_id)):
            current_players = self.player.db_player.get(query.id == list_player_id[i])
            self.players_extracted.append(current_players)
        return self.players_extracted

    def player_report(self):
        print("-" * 80)
        print(" --------------------------- Rapport des joueurs  --------------------------- ")
        print("-" * 80)
        print("A - Joueurs classés par ordre alphabétique :")
        players_info = self.player.db_player.all()
        players_info = sorted(players_info, key=lambda x: x['Nom'])
        for i in players_info:
            players_unserialized = self.player.unserialized(i)

            print(
                f" {players_unserialized.first_name} {players_unserialized.last_name} -"
                f" {players_unserialized.birth_date}"
                f" - {players_unserialized.gender} - Classement : {players_unserialized.rank}")

        print("-" * 80)
        print("B - Joueurs listés par classement:")
        players_info = list(self.player.db_player.all())
        players_info = sorted(players_info, key=lambda x: int(x['Classement']), reverse=True)

        for i in players_info:
            players_unserialized = self.player.unserialized(i)

            print(
                f"Classement : {players_unserialized.rank} - {players_unserialized.last_name}"
                f" {players_unserialized.first_name} - {players_unserialized.birth_date}"
                f" - {players_unserialized.gender} ")

        print("-" * 80)
        print("C - Liste de tous les joueurs d'un tournoi par ordre alphabétique :")

        query = Query()
        tournoi_info = self.tournoi.db_tournoi.all()

        # self.player.db_player.update({'Score': match.score_player2}, query.id == match.player2['id'])

        for i in tournoi_info:
            tournois_unserialized = self.tournoi.unserialized(i)
            print(
                f": {tournois_unserialized.name} - {tournois_unserialized.date}"
                f" {tournois_unserialized.player_list} - Description: {tournois_unserialized.description}")

        print("-" * 80)
        print("D - Liste de tous les joueurs d'un tournoi par classement :")

        for i in tournoi_info:
            tournois_unserialized = self.tournoi.unserialized(i)
            print(
                f": {tournois_unserialized.name} - {tournois_unserialized.tour_list}")

    def update_rank(self):
        """
        Cette fonction permet de mettre à jour le classement d'un joueur à partir du menu principale.
        """
        self.player = player.Player()
        valid_name = False
        while not valid_name:
            player_id = input("Merci de saisir l'id du joueur à mettre à jour ")
            if player_id.isdigit():
                valid_name = True
            else:
                print("Erreur: Merci de saisir un id valid")

            valid_rank = False
            while not valid_rank:
                rank = input("Merci de saisir le nouveau classement: ")
                if rank.isdigit() and int(rank) >= 0:

                    valid_rank = True
                    # player = player.db_player.update(query.id == int(player_id))
                    query = Query()
                    self.player.db_player.update({'Classement': int(rank)}, query.id == int(player_id))
                else:
                    print("Erreur: merci de saisir un chiffre positif")
                print("----> Message info : le classement a été mis à jour dans la base de données")


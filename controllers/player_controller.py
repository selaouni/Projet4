from controllers import base_controller


class CreatePlayerController:

    def __init__(self):
        self.player_value = []
        self.player_info = ["Nom", "Prénom", "Date de naissance", "Genre", "Classement"]
        self.main_controller_menu = base_controller.MainMenuController()

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

        valid_day = False
        while not valid_day:
            self.birth_day = input("Entrez le jour de naissance du joueur: ")
            if  len(self.birth_day) == 2 and int(self.birth_day) < 32 and self.birth_day.isdigit():
                valid_day = True
                birthdate_list.append(self.birth_day)
            else:
                print("Erreur: Merci de saisir un jour de naissance valide en 2 chiffres")

        valid_month = False
        while not valid_month:
            self.birth_month = input("Entrez le mois de naissance En chiffre: ")
            if  len(self.birth_month) == 2 and int(self.birth_month) < 13 and self.birth_month.isdigit():
                valid_month = True
                birthdate_list.append(self.birth_month)
            else:
                print("Erreur: Merci de saisir un nombre à 2 chiffres <= 12")

        valid_year = False
        while not valid_year:
            self.birth_year = input("Entrez l'année de naissance du joueur: ")
            if  len(self.birth_year) == 4 and int(self.birth_year) < 2023 and self.birth_year.isdigit():
                valid_year = True
                birthdate_list.append(self.birth_year)
            else:
                print("Erreur: Merci de saisir une année de naissance valide (en 4 chiffres)")

        return f"{birthdate_list[0]}/{birthdate_list[1]}/{birthdate_list[2]}"

    def add_gender(self):
        valid_gender = False
        validated_gender = None
        while not valid_gender:
            gender = input("Saisir le genre du joueur 'Homme' ou 'Femme'")

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
            rank = input("Saisir le classement du joueur: ")
            if rank.isdigit() and int(rank) >= 0:
                valid_rank = True
            else:
                print("Erreur: Merci de saisir un nombre entier positif")
        return int(rank)




    def __call__(self):

        self.player_model = player.Player()
        self.player_value.append(self.add_last_name())
        self.player_value.append(self.add_first_name())
        self.player_value.append(self.add_birth_date())
        self.player_value.append(self.add_gender())
        self.player_value.append(self.add_rank())
        self.main_controller_menu()

class Player_Report:
        pass


"""
Player_object = CreatePlayerController()
Player_FirstName= CreatePlayerController.add_first_name(self=Player_object)
Player_lastName = CreatePlayerController.add_last_name(self=Player_object)
Player_BirthDate= CreatePlayerController.add_birth_date(self=Player_object)
Player_Gender = CreatePlayerController.add_gender(self=Player_object)
Player_Ranking = CreatePlayerController.add_ranking(self=Player_object)
print(Player_FirstName)
print(Player_lastName)
print(Player_BirthDate)
print(Player_Gender)
print(Player_Ranking)
"""
















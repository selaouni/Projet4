from tinydb import TinyDB


class Player:
    def __init__(self, first_name = None, last_name = None, birth_Date = None, gender = None, rank = 0, score = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_Date = birth_Date
        self.gender = gender
        self.rank = rank
        self.score = score

        self.db_player = TinyDB('DB_players.json')


    def serialize(self):
        player_information = {}
        player_information['Nom'] = self.last_name
        player_information['Prenom'] = self.first_name
        player_information['Date de naissance'] = self.birth_Date
        player_information['Genre'] = self.gender
        player_information['Classement'] = self.rank
        player_information['Score'] = self.score
        return player_information


    def save_player(self, player_info):
        player = Player(player_info[0],
                        player_info[1],
                        player_info[2],
                        player_info[3],
                        player_info[4]
                        )
        db_player = self.db_player
        db_player.insert(player.serialize())


    def update_rank(self):
        valid_name = False
        while not valid_name:
            player_name = input("Entrer le nom de famille du joueur : ")
            if player_name.isalpha():
                valid_name = True
            else:
                print("Erreur: Merci de saisir un nom de famille valid")

        valid_rank = False
        while not valid_rank:
            rank = input("Saisir le nouveau classement du joueur: ")
            if rank.isdigit() and int(rank) >= 0:
                valid_rank = True
                self.db_player.update({'classement': self.rank},self.last_name == player_name)
            else:
                print("Erreur: merci de saisir un chiffre positif")
            return rank



from tinydb import TinyDB, Query


class Player:
    def __init__(self, id=0,
                 first_name=None,
                 last_name=None,
                 birth_date=None,
                 gender=None,
                 rank=0,
                 score=0.0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = int(rank)
        self.score = int(score)

        self.db_player = TinyDB('DB_players.json')

    def __str__(self):
        return f"{self.id} - {self.last_name} - {self.first_name} - Classement - {self.rank}."

    def serialize(self):
        player_information = {}
        player_information['id'] = int(self.id)
        player_information['Prenom'] = self.first_name
        player_information['Nom'] = self.last_name
        player_information['Date de naissance'] = self.birth_date
        player_information['Genre'] = self.gender
        player_information['Classement'] = self.rank
        player_information['Score'] = int(self.score)
        return player_information

    def save_player(self, player_info):
        """
        :param : Liste avec les informations player
        Cette fonction permet de sauvegarder les instances serialisées de player dans
        la base de données "DB_players.json"
        """
        player = Player(player_info[0],
                        player_info[1],
                        player_info[2],
                        player_info[3],
                        player_info[4],
                        player_info[5],
                        player_info[6],
                        )
        db_player = self.db_player
        db_player.insert(player.serialize())

    def unserialized(self, serialized_player):
        id = serialized_player["id"]
        first_name = serialized_player["Prenom"]
        last_name = serialized_player["Nom"]
        birth_date = serialized_player["Date de naissance"]
        gender = serialized_player["Genre"]
        ranking = serialized_player["Classement"]
        score = serialized_player["Score"]

        return Player(id,
                      last_name,
                      first_name,
                      birth_date,
                      gender,
                      ranking,
                      score,
                      )




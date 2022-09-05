from tinydb import TinyDB



class Player:
    def __init__(self, id = 0,  first_name=None, last_name = None, birth_Date = None, gender = None, rank = 0, score = 0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_Date = birth_Date
        self.gender = gender
        self.rank = rank
        self.score = score

        self.db_player = TinyDB('DB_players.json')


    def serialize(self):
        player_information = {}
        player_information['id'] = self.id
        player_information['Prenom'] = self.first_name
        player_information['Nom'] = self.last_name
        player_information['Date de naissance'] = self.birth_Date
        player_information['Genre'] = self.gender
        player_information['Classement'] = int(self.rank)
        player_information['Score'] = int(self.score)
        return player_information


    def save_player(self, player_info):
        player = Player(player_info[0],
                        player_info[1],
                        player_info[2],
                        player_info[3],
                        player_info[4],
                        player_info[5],

                        )
        db_player = self.db_player
        db_player.insert(player.serialize())

    def unserialized(self, serialized_player):
        id = serialized_player["id"]
        first_name = serialized_player["prenom"]
        last_name = serialized_player["nom"]
        birth_Date = serialized_player["Date de naissance"]
        gender = serialized_player["genre"]
        ranking = serialized_player["Classement"]
        score = serialized_player["Score"]

        return Player(id,
                      last_name,
                      first_name,
                      birth_Date,
                      gender,
                      ranking,
                      score,
                      )

    def show(self):

        print("nom:" + self.first_name)
        print("prenom:" + self.last_name)
        print("date de naissance:" + self.birth_Date)
        print("sexe:" + self.gender)
        print("classement:" + str(self.rank))

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
                db_player = self.db_player
                db_player.update({'Classement': self.rank})
                #self.db_player.update({'Classement': self.rank},self.last_name == player_name)

            else:
                print("Erreur: merci de saisir un chiffre positif")
            return rank



class Player:
    def __init__(self, first_name, last_name, birth_Date, gender, rank, score):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_Date = birth_Date
        self.gender = gender
        self.rank = rank
        self.score = score

    def create_player (self):
        player_information = {}
        player_information['Nom'] = self.last_name
        player_information['Prenom'] = self.first_name
        player_information['Date de naissance'] = self.birth_Date
        player_information['Genre'] = self.gender
        player_information['Classement'] = self.rank
        player_information['Score'] = self.score
        return player_information


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
            else:
                print("Erreur: merci de saisir un chiffre positif")
            return rank


"""
player = Player( 'Sabah', 'ELAOUNI', 1985, 'Femme', 1, 10)
creation_joueur = Player.create_player(self=player)
print ("Nom: ",player.first_name)
print ("Prénom: ",player.last_name)
print ("Date de naissance: ",player.birth_Date)
print ("genre: ",player.gender)
print ("classement: ",player.rank)
print ("score: ",player.score)
print(creation_joueur)
MiseAjour =  player.update_ranking()
"""
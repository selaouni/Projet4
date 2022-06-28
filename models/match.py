from models.tour import Tours
from models.player import Player

class Matchs:
    def __init__(self, match_number, player1, player2, score_player1, score_player2):
        self.match_number = match_number
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2


    def add_Match(self):
        Match_information = {}
        Match_information['premier joueur'] = self.player1
        Match_information['2eme joueur'] = self.player2
        Match_information['Score 1eme joueur'] = self.score_player1
        Match_information['Score 2eme joueur'] = self.score_player2
        return Match_information

    def match_pairing(self, player1, player2):
        match = (f"{player1['Nom']}",player1["Classement"], player1["score"],f"{player2['Nom']}",player2["Classement"],player2["score"])

        match_list_instance = Tours()
        match_list_instance.match_list.append(match)
        print (match)


    def __str__(self):
        return f"{self.match_number} : {self.player1} --CONTRE-- {self.player2}."

x = Matchs("K045","Sabah", "Sara", 1, 1)
print(x)
P1 = Player("Sabah","ELAOUNI","07081985",Femme,1,10)
P2 = Player("Sara","ELAOUNI","07081994",Femme,1,10)
z= x.match_pairing(P1,P2)
print(z)

from models.tour import Tours
from models.player import Player

class Matchs:
    def __init__(self, match_number, player1, player2, score_player1, score_player2):
        self.match_number = match_number
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def __str__(self):
        return f"{self.match_number} : {self.player1} --CONTRE-- {self.player2}."

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


    def match_result(self):
        match_list = []
        date_list.append(self.birth_year)
        valid_score1= False
        while not valid_score1:
            score_player1 = input("Saisir le score du premier joueur (gagnant = 1), (match nul = 0,5),(pardant = 0)  :")

            if score_player1 != 1 and score_player1 != 0.5 and score_player1 != 0:
                print("Erreur: Merci de saisir  comme score : 1, 0.5, ou 0")
            else:
                self.score_player1 = score_player1


        valid_score2 = False
        while not valid_score2:
            score_player2 = input("Saisir le score du deuxieme joueur (gagnant = 1), (match nul = 0,5),(pardant = 0): ")

            if score_player2 != 1 and score_player2 != 0.5 and score_player2 != 0:
                print("Erreur: Merci de saisir  comme score : 1, 0.5, ou 0")
            else:
                self.score_player2 = score_player2

        return match_list.append(self.score_player1,self.score_player2)








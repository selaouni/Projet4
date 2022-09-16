

class Matchs:
    def __init__(self, match_number=0,
                 player1=None,
                 player2=None,
                 score_player1=0,
                 score_player2=0):
        self.match_number = match_number
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def serialize(self):
        Match_information = {}
        Match_information['premier joueur'] = self.player1
        Match_information['2eme joueur'] = self.player2
        Match_information['Score 1eme joueur'] = self.score_player1
        Match_information['Score 2eme joueur'] = self.score_player2
        return Match_information

    def __str__(self):
        return f"{self.match_number} : {self.player1} --CONTRE-- {self.player2}."

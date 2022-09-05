from models import match

class Tours:
    def __init__(self,tour_name, match_list,  Date_Time_Start, Date_Time_End):
        self.tour_name = tour_name
        self.match_list = []
        self.Date_Time_Start = Date_Time_Start
        self.Date_Time_End = Date_Time_End
        self.match = match.Matchs()


    def create_tour(self):
        tour_information = {}
        tour_information['Tour name'] = self.tour_name
        tour_information['Matchs'] = self.match_list
        tour_information['begining'] = self.Date_Time_Start
        tour_information['end'] = self.Date_Time_End
        return tour_information

    def __repr__(self):
        return f"{self.tour_name} - Début : {self.Date_Time_Start}. Fin : {self.Date_Time_End}."

    def pairing(self, player1, player2):
        match = (
            f"{player1['Nom']}, {player1['prenom']}",
            player_1["classement"],
            player_1["score"],
            f"{player2['nom']}, {player2['prenom']}",
            player_2["classement"],
            player_2["score"]
        )
        self.match_list.append(match)

    # liste des joueurs deja filtré (sorted player)
    # methode diviser


    def run(self, sorted_players, tournoi_object):

        self.list_tour = []
        self.match_list = []
        self.name = "Round " + str(len(tournoi_object.list_tours) + 1) # num tour + 1

        # while len(sorted_players) > 0:
        #     match_object = match(self.name, sorted_players[0], sorted_players[4])

        while len(sorted_players) > 0:
            match_object = match(self.name, sorted_players[0], sorted_players[1])
            self.list_tour.append(match_object)
            del sorted_players[0:2]

        for match in self.list_tour:

            valid_score_player1 = False
            while not valid_score_player1:
                score_player1 = input(f"saisir le score de {match.player1} :")
                float(score_player1)
                if  score_player1 != 0 or score_player1 != 0.5 or score_player1 != 1:
                    print("Erreur: merci de saisir --> 0, 0.5, ou 1")
                else:
                    match.score_player_1 = float(score_player1)
                    match.player1.tournament_score += float(score_player_1)
                    valid_score_player1 = True

            valid_score_player2 = False
            while not valid_score_player2:
                score_player2 = input(f"saisir le score de {match.player2} :")
                float(score_player2)
                if  score_player2 != 0 or score_player2 != 0.5 or score_player2 != 1:
                    print("Erreur: merci de saisir --> 0, 0.5, ou 1")
                else:
                    match.score_player2 = float(score_player2)
                    match.player2.tournoi_score += float(score_player2)
                    valid_score_player2 = True

            self.match_list.append(([match.player1.player_id, match.score_player1],
                                                 [match.player2.player_id, match.score_player2]))

        return Tour(self.name, self.match_list)


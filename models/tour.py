
class Tours:
    def __init__(self,tour_name, match_list,  Date_Time_Start, Date_Time_End):
        self.tour_name = tour_name
        self.match_list = []
        self.Date_Time_Start = Date_Time_Start
        self.Date_Time_End = Date_Time_End


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



    def run_tour(self, players_list, tournoi_instance):
        pass










)
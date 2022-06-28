
class Tours:
    def __init__(self,tour_name, match_list,  Date_Time_Start, Date_Time_End):
        self.tour_name = tour_name
        self.match_list = match_list
        self.Date_Time_Start = Date_Time_Start
        self.Date_Time_End = Date_Time_End
        self.list_of_tours = [] # ??

    def create_tour(self):
        tour_information = {}
        tour_information['Tour name'] = self.tour_name
        tour_information['Matchs'] = self.match_list
        tour_information['begining'] = self.Date_Time_Start
        tour_information['end'] = self.Date_Time_End
        return tour_information

    def __repr__(self):
        return f"{self.tour_name} - Début : {self.Date_Time_Start}. Fin : {self.Date_Time_End}."


    def run_tour(self, players_list, tournoi_instance):
        pass












"""   
    def create_matchs(self):
        matchs = []
        for i, pair in enumerate(self.match_list):
            matchs.append(Match(name=f"Match {i}", match_list=pair))
        return matchs

    # ??
    def Generate_pair (self):
        self.match_list = []
        numero = [1,2,3,4]
        for i in numero:
            print("entrer les paires de joueurs numéro :" , i)
            self.match_list.append(match_instance)
"""


tour = Tours('Mon tour', 'liste des matchs',  '1022022 11:03', '1022022 15:00')
AjouterTour = Tours.create_tour(self=tour)
print(tour.tour_name)
print(tour.match_list ,"...")
print(tour.Date_Time_Start)
print(tour.Date_Time_End)
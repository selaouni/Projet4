from tinydb import TinyDB


class Tournoi:
    def __init__(self, name = None, date = None, place = None, nbr_tours = 4 , tour_list = [] ,
                 player_list = [], description =None,  timing = None):
        self.name = name
        self.place = place
        self.date = date
        self.nbr_tours = nbr_tours
        self.tour_list = tour_list
        self.player_list = player_list
        self.timing = timing
        self.description = description

        self.db_tournoi= TinyDB('DB_tournoi.json')


    def serialize(self):
        Tournoi_information = {}
        Tournoi_information['nom du tournoi'] = self.name
        Tournoi_information['Place'] = self.place
        Tournoi_information['Date'] = self.date
        Tournoi_information['Numbre of tours'] = self.nbr_tours
        Tournoi_information['liste joueurs']=self.player_list
        Tournoi_information['Time control'] = self.timing
        Tournoi_information['Résultat'] = self.description
        Tournoi_information["liste des Tours"] = self.tour_list
        return Tournoi_information

    def save_tournoi(self, tournoi_info):
        tournoi = Tournoi(tournoi_info[0],
                        tournoi_info[1],
                        tournoi_info[2],
                        tournoi_info[3],
                        tournoi_info[4],
                        tournoi_info[5],
                        tournoi_info[6],)
        db_tournoi = self.db_tournoi
        db_tournoi.insert(tournoi.serialize())

    def __repr__(self):
        return f"{self.name} - {self.place} - {self.tour_list} - {self.timing} \n"

    def show_all(self):
        print(self.db_tournoi.all())

    def start_tournament(self, t):
        pass

    def first_round(self, t):
        pass

    def next_rounds(self, t):
        pass

    def match_first_option(self, available_list, players_added, r):
        pass

    def match_other_option(self, available_list, players_added, r):
        pass

    def end_of_round(self, scores_list: list, t):
        pass

    def input_scores(self):
        pass

    def get_score(self, response, scores_list: list):
        pass






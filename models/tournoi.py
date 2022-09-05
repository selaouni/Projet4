from tinydb import TinyDB
import pandas as pd


class Tournoi:
    def __init__(self, name = None,  place = None, date = None, nbr_tours = 4 ,player_list = [], tour_list = []
                 , description =None,  timing = None):
        self.name = name
        self.place = place
        self.date = date
        self.nbr_tours = nbr_tours
        self.player_list = player_list
        self.tour_list = tour_list
        self.timing = timing
        self.description = description
        self.db_tournoi = TinyDB('DB_tournoi.json')


    def serialize(self):
        Tournoi_information = {}
        Tournoi_information['nom du tournoi'] = self.name
        Tournoi_information['Place'] = self.place
        Tournoi_information['Date'] = self.date
        Tournoi_information['liste joueurs']=self.player_list
        Tournoi_information['Numbre of tours'] = self.nbr_tours
        Tournoi_information['Time control'] = self.timing
        Tournoi_information['Remarques'] = self.description
        Tournoi_information["liste des Tours"] = self.tour_list
        return Tournoi_information

    def save_tournoi(self, tournoi_info):
        tournoi = Tournoi(tournoi_info[0],
                        tournoi_info[1],
                        tournoi_info[2],
                        tournoi_info[3],
                        tournoi_info[4],
                        tournoi_info[5],
                        tournoi_info[6])
        db_tournoi = self.db_tournoi
        db_tournoi.insert(tournoi.serialize())



    def sorted_first_time(self,list_player_to_sort):
        player_list = pd.DataFrame(list_player_to_sort)
        player_list = player_list.sort_values(('Classement'),ascending=False)
        self.player_list = player_list.T.to_dict().values()
        return(self.player_list)



    def split(self,sorted_player_to_split):

        half = len(sorted_player_to_split) // 2
        player_splitted = sorted_player_to_split[:half],sorted_player_to_split[half:]
        print("player split", player_splitted)
        return (player_splitted)

    def make_match(self, player_splitted1 ,player_splitted2):

        match_players = []
        for i in range(len(self.player_list) // 2):
            match_players.append(player_splitted1[i])
            match_players.append(player_splitted2[i])
        print("les matchs sont comme suit : ",match_players)
        return player_splitted1, player_splitted2

    def sorted_second_time(self,):
        pass




    def run_tournoi(self):

        self.sorted_first_time()
        self.sorted_second_time()









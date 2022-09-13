from models import player
from models import match
from models import tour
from tinydb import TinyDB, Query

import pandas as pd


class Tournoi:
    def __init__(self, name=None, place=None, date=None, nbr_tours = 4, player_list = [], timing=None,
                 description=None, tour_list=()):

        self.name = name
        self.place = place
        self.date = date
        self.nbr_tours = nbr_tours
        self.player_list = player_list
        self.timing = timing
        self.description = description
        self.tour_list = tour_list
        self.player = player.Player()
        self.match = match.Matchs()
        self.tour = tour.Tours()
        self.players_extracted = []

        self.db_tournoi = TinyDB('DB_tournoi.json')



    def serialize(self):
        Tournoi_information = {}
        Tournoi_information['nom du tournoi'] = self.name
        Tournoi_information['Place'] = self.place
        Tournoi_information['Date'] = self.date
        Tournoi_information['Numbre of tours'] = self.nbr_tours
        Tournoi_information['liste joueurs']=self.player_list
        Tournoi_information['Time control'] = self.timing
        Tournoi_information['Remarques'] = self.description
        Tournoi_information['liste des Tours'] = self.tour_list
        return Tournoi_information

    def save_tournoi(self, tournoi_info):
        tournoi = Tournoi(tournoi_info[0],
                        tournoi_info[1],
                        tournoi_info[2],
                        tournoi_info[3],
                        tournoi_info[4],
                        tournoi_info[5],
                        tournoi_info[6],
                        tournoi_info[7])
        db_tournoi = self.db_tournoi
        db_tournoi.insert(tournoi.serialize())


    def unserialized(self, serialized_tournoi):
        name = serialized_tournoi["nom du tournoi"]
        place = serialized_tournoi["Place"]
        date = serialized_tournoi["Date"]
        nbr_tours = serialized_tournoi["Numbre of tours"]
        player_list = serialized_tournoi["liste joueurs"]
        timing = serialized_tournoi["Time control"]
        description = serialized_tournoi["Remarques"]
        tour_list = serialized_tournoi["liste des Tours"]

        return Tournoi(name,
                      place,
                      date,
                      nbr_tours,
                      player_list,
                      timing,
                      description,
                      tour_list,
                      )


    def get_info_by_id(self, list_player_id):

        query = Query()
        for i in range(len(list_player_id)):
            current_players = self.player.db_player.get(query.id == list_player_id[i])
            self.players_extracted.append(current_players)
        return self.players_extracted

    def sorted_first_time(self,list_player_to_sort):
        player_list = pd.DataFrame(list_player_to_sort)
        player_list = player_list.sort_values(("Classement"), ascending=False)
        self.player_list = player_list.T.to_dict().values()
        return(self.player_list)

    def split(self,sorted_player_to_split):

        half = len(sorted_player_to_split) // 2
        player_splitted = sorted_player_to_split[:half], sorted_player_to_split[half:]
        return player_splitted


    def make_match(self, players_list1, players_list2):

        players_match = []
        for i in range(len(self.player_list) // 2):
            players_match.append(players_list1[i])
            players_match.append(players_list2[i])
        self.player_list = players_match
        print("------ matchs constitués : ")
        for i in range(0 ,(self.nbr_tours * 2), 2):
            print(players_match[i], players_match[i+1])
        return self.player_list

    #Sort players by score
    def sorted_second_time(self,tour_list):
        players_with_score = []
        players_sorted_by_score = []
        players_id = []
        tour_object = []
        players_object = []
        #info_player = []
        players_by_score = []

        for i in range(len(tour_list)):
            tour_object = self.tour.unserialize(tour_list)


        for match in tour_object.match_list:
            for player in match:
                players_with_score.append(player)

        for player in players_sorted_by_score:
            players_id.append(player[0])

        info_player = self.get_info_by_id(players_id)
        # for i in range(len(info_player)):
        #     players_object = self.player.unserialized(info_player[i])
        player_list = pd.DataFrame(info_player)
        player_list = player_list.sort_values(by=['Score', 'Classement'], ascending=False)
        players_by_score = player_list.T.to_dict().values()
        return players_by_score

    def run_tour1(self):
        self.tour_list = self.tour.run(self.player_list, Tournoi())

        return self.tour_list
    def run_other_tours(self):
        print("-"*80)
        print ("self.tour_list test", self.tour_list)
        print("-"*80)
        # sorted_players = self.sorted_second_time(self.tour_list)
        # print("-" * 80)
        # print("sorted players_next tour", sorted_players)
        # print("-" * 80)
        for i in range(int(self.nbr_tours) - 1):
            # self.sorted_players.clear()
            self.tournoi_object = Tournoi()
            self.tournoi_object.tour_list = []

            sorted_players = self.sorted_second_time(self.tour_list[i])
            print("-" * 80)
            print("Joueurs triés par score puis par classement test",sorted_players)
            print("-" * 80)

            self.tournoi_object.tour_list.append(self.tour.run(list(sorted_players), self.tournoi_object))





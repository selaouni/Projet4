from models import match
from models import player
from datetime import datetime
from tinydb import Query


class Tours:
    def __init__(self,tour_name = None, match_list =None,  date_time_start = None, date_time_end=None):
        self.tour_name = tour_name
        self.match_list = match_list
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.match = match.Matchs
        self.player = player.Player()
        self.player1 = player.Player()
        self.player2 = player.Player()
        self.player_value = []

    def serialize(self):
        tour_information= {}
        tour_information['Nom du tour'] = self.tour_name
        tour_information['Liste des Matchs'] = self.match_list
        tour_information['Date et heure debut'] = self.date_time_start
        tour_information['Date et heure fin'] = self.date_time_end
        return tour_information

    def unserialize(self, serialized_tour):
        name = serialized_tour["Nom du tour"]
        match_list = serialized_tour["Liste des Matchs"]
        date_time_start = serialized_tour["Date et heure debut"]
        date_time_end = serialized_tour["Date et heure fin"]

        return Tours(name,
                     match_list,
                     date_time_start,
                     date_time_end,
                     )
    def run(self, match_list, tournoi_object):

        self.Date_Time_Start = datetime.now()
        print("Tour lancé à : ", self.Date_Time_Start)
        self.tour_name= "Tour " + str(len(tournoi_object.tour_list) + 1)
        self.list_tour = []
        self.match_list = []

        while len(match_list) > 0:
            match = self.match(self.tour_name, match_list[0], match_list[1]) # création de l'objet match

            self.player1.unserialized(match_list[0])
            self.player2.unserialized(match_list[1])

            self.list_tour.append(match)
            del match_list[0:2]
        print("saisie pour le ",  self.tour_name, " --> ")
        for match in self.list_tour:
            score_player1 = float(input("Merci de saisir le score du premier joueur  : "))
            match.score_player1 = score_player1
            self.player1.score = score_player1


            score_player2 = input("Merci de saisir le score du deuxiem joueur : ")
            match.score_player2 = float(score_player2)
            self.player2.score = float(score_player2)



            #self.player2.save_player(self.player2)
            #match.player2.score += float(score_player2)
            # valid_score_player1 = False
            # while not valid_score_player1:
            #
            #     score_player1 = input("Merci de saisir le score du premier joueur : ")
            #     float(score_player1)
            #     if score_player1 != 1 or score_player1 != 0 or score_player1 != 0:
            #         print("Erreur: merci de saisir --> 1, 0, ou 0.5")
            #     else:
            #         Matchs.score_player_1 = float(score_player1)
            #         #Matchs.player1.tournament_score += float(score_player_1)
            #         valid_score_player1 = True
            #
            # valid_score_player2 = False
            # while not valid_score_player2:
            #     score_player2 = input("Merci de saisir le score du deuxiem joueur : ")
            #     float(score_player2)
            #     if score_player2 != 1 or score_player2 != 0 or score_player1 != 0:
            #     # score_player2 == "" and score_player2.isalpha():
            #         print("Erreur: merci de saisir --> 1, 0, ou 0.5")
            #     else:
            #         Matchs.score_player2 = float(score_player2)
            #         #match.player2.tournoi_score += float(score_player2)
            #         valid_score_player2 = True

            self.match_list.append(([match.player1['id'], match.score_player1],[match.player2['id'], match.score_player2]))
            print("Résultats pris en compte : ", self.match_list)




        self.Date_Time_End = datetime.now()
        print("Tour terminé à : ", self.Date_Time_End)
        tour_object = Tours(self.tour_name, self.match_list, str(self.Date_Time_Start), str(self.Date_Time_End))
        query = Query()
        self.player.db_player.update({'Score': match.score_player1}, query.id == match.player1['id'])
        self.player.db_player.update({'Score': match.score_player2}, query.id == match.player2['id'])
        tour_serialized = []

        tour_serialized.append(tour_object.serialize())
        return tour_serialized



from tinydb import TinyDB


class Tournoi:
    def __init__(self, name=None,
                 place=None,
                 date=None,
                 nbr_tours=4,
                 player_list=None,
                 timing=None,
                 description=None,
                 tour_list=()):

        self.name = name
        self.place = place
        self.date = date
        self.nbr_tours = nbr_tours
        self.player_list = player_list
        self.timing = timing
        self.description = description
        self.tour_list = tour_list
        self.db_tournoi = TinyDB('DB_tournoi.json')

    def serialize(self):
        Tournoi_information = {}
        Tournoi_information['nom du tournoi'] = self.name
        Tournoi_information['Place'] = self.place
        Tournoi_information['Date'] = self.date
        Tournoi_information['Numbre of tours'] = self.nbr_tours
        Tournoi_information['liste joueurs'] = self.player_list
        Tournoi_information['Time control'] = self.timing
        Tournoi_information['Remarques'] = self.description
        Tournoi_information['liste des Tours'] = self.tour_list
        return Tournoi_information

    def save_tournoi(self, tournoi_info):
        """
        :param : Liste avec les informations du tournoi
        Cette fonction permet de sauvegarder les instances serialisées d'un tournoi dans
        la base de données "DB_tournoi.json"
        """
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




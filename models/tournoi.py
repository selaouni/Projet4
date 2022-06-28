


class Tournoi:
    def __init__(self, name, date, place, nbr_tours , tour_list , player_list , description,  time_control):
        self.name = name
        self.place = place
        self.date = date
        self.nbr_tours = nbr_tours
        self.tour_list = tour_list
        self.player_list = player_list
        self.time_control = time_control
        self.description = description


    def creation_Tournoi (self):
        self.Tournoi_information = {}
        Tournoi_information['nom du tournoi'] = self.name
        Tournoi_information['Place'] = self.place
        Tournoi_information['Date'] = self.date
        Tournoi_information['Numbre of tours'] = self.nbr_tours
        Tournoi_information['Time control'] = self.time_control
        Tournoi_information['Résultat'] = self.description
        Tournoi_information["liste des Tours"] = self.tour_list
        return Tournoi_information

    def __repr__(self):
        return f"{self.name} - {self.place} - {self.tour_list}\n"


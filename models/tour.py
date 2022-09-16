

class Tours:
    def __init__(self, tour_name=None, match_list=None, date_time_start=None, date_time_end=None):
        self.tour_name = tour_name
        self.match_list = match_list
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end


    def serialize(self):
        tour_information = {}
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
                     date_time_end,)


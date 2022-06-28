from views import menu
from controllers import player_controller
from controllers import tournoi_controller
from models import player


class MainMenuController:

    def __init__(self):
        self.first_view = menu.FirstTitles()
        self.menu_display = menu.Menu()
        self.option = None

    def __call__(self):
        self.first_view.Titles()
        data = self.menu_display(self.menu_display.main_menu)

        if data == "1":
            self.option = PlayerController_Menu()
            self.player_menu_controller_redirect()

        if data == "3":
            self.option = TournoiController_Menu()
            self.tournoi_menu_controller_redirect()

    def player_menu_controller_redirect(self):
        return self.option()

    def tournoi_menu_controller_redirect(self):
        return self.option()

class PlayerController_Menu():

    def __init__(self):
        self.main_controller_menu = MainMenuController()
        self.player_controller = player_controller.CreatePlayerController()
        self.player_model = player.Player()
        self.menu_display = menu.Menu()
        self.player_report = player_controller.Player_Report()

    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "1":
            self.option = self.player_controller()
        if data == "2":
            self.option = self.player_model.update_rank()



class TournoiController_Menu():

    def __init__(self):
        self.tournoi_controller = tournoi_controller.CreateTournoiController()
        self.menu_display = menu.Menu()
        self.run_tournoi = tournoi_controller.Tournoi_run
        self.tournoi_report= tournoi_controller.TournoiReport()

    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "3":
            self.option = self.tournoi_controller()
        if data == "4":
            self.option = self.run_tournoi()


class Report_menu:
    pass
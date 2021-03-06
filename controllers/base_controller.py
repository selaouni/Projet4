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
            self.option = PlayerControllerMenu()
            self.player_menu_controller_redirect()

        if data == "2":
            self.option = RankControllerMenu()
            self.rank_menu_controller_redirect()

        if data == "3":
            self.option = TournoiControllerMenu()
            self.tournoi_menu_controller_redirect()

        if data == "4":
            pass

        if data == "5":
            self.option = ReportControllerMenu()
            self.report_menu_controller_redirect()

        if data == "6":
            self.option = ReportControllerMenu()
            self.report_menu_controller_redirect()


    def player_menu_controller_redirect(self):
        return self.option()

    def tournoi_menu_controller_redirect(self):
        return self.option()

    def report_menu_controller_redirect(self):
        return self.option()

    def rank_menu_controller_redirect(self):
        return self.option()

class PlayerControllerMenu:

    def __init__(self):
        self.main_controller_menu = MainMenuController()
        self.player_controller = player_controller.CreatePlayerController()
        self.player_model = player.Player()
        self.menu_display = menu.Menu()


    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "1":
            self.option = self.player_controller()
        if data == "2":
            self.option = self.player_model.update_rank()




class TournoiControllerMenu:

    def __init__(self):
        self.tournoi_controller = tournoi_controller.CreateTournoiController()
        self.menu_display = menu.Menu()
        self.run_tournoi = tournoi_controller.Tournoi_run


    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "3":
            self.option = self.tournoi_controller()
        if data == "4":
            self.option = self.run_tournoi()





class ReportControllerMenu:

    def __init__(self):
        self.player_controller = player_controller.CreatePlayerController()
        self.player_report = player_controller.Player_Report()
        self.tournoi_report = tournoi_controller.TournoiReport()
        self.menu_display = menu.Menu()

    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "5":
            self.option = self.player_report()
        if data == "6":
            self.option = self.tournoi_report()


class RankControllerMenu():

    def __init__(self):
        self.player_controller = player_controller.CreatePlayerController()
        self.menu_display = menu.Menu()
        self.rank_menu = player_controller.CreatePlayerController.add_rank()

    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "2":
            self.option = self.rank_menu



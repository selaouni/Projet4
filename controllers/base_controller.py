from views import menu
from controllers import player_controller
from controllers import tournoi_controller
from models import player


class MainMenuController:
    """
    Dans cette classe on appelle les differentes classes du module "views", ce qui va permettre d'afficher d'abord
    le menu principal et puis d'etre redirigé vers les sous menu associés
    """

    def __init__(self):
        self.first_view = menu.First_titles()
        self.menu_display = menu.Menu()
        self.option = None

    def __call__(self):
        self.first_view.titles()
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
            self.option = RepriseTournoi()
            self.reprise_menu_controller_redirect()

        if data == "5":
            self.option = ReportControllerMenu()
            self.report_menu_controller_redirect()

        if data == "6":
            self.option = ReportControllerMenu()
            self.report_menu_controller_redirect()

        if data == "7":
            exit()

    def player_menu_controller_redirect(self):
        return self.option()

    def tournoi_menu_controller_redirect(self):
        return self.option()

    def report_menu_controller_redirect(self):
        return self.option()

    def reprise_menu_controller_redirect(self):
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
        # self.tour = tour.Tours()
        self.tournoi_controller = tournoi_controller.CreateTournoiController()
        self.menu_display = menu.Menu()
        # self.run_tournoi = tour.Tours.run()

    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "3":
            self.option = self.tournoi_controller()


class RepriseTournoi():
    def __init__(self):
        self.menu_display1 = menu.Menu()
        self.menu_display2 = menu.ReLoadTournament()

    def __call__(self):

        data = self.menu_display1(self.menu_display1.main_menu)
        if data == "4":
            self.option = self.menu_display2()
            print("test")


class ReportControllerMenu:

    def __init__(self):
        self.player_controller = player_controller.CreatePlayerController()
        self.menu_player_report = menu.Player_report()
        self.menu_tournoi_report = menu.Tournoi_report()
        self.menu_display = menu.Menu()

    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "5":
            self.option = self.menu_player_report()
        if data == "6":
            self.option = self.menu_tournoi_report()


class RankControllerMenu():
    def __init__(self):

        self.player_controller = player_controller.CreatePlayerController()
        self.menu_display = menu.Menu()
        self.rank_menu = player.Player.update_rank(player.Player)

    def __call__(self):
        data = self.menu_display(self.menu_display.main_menu)
        if data == "2":
            self.option = self.rank_menu()

from controllers import base_controller



def main():

    controller = base_controller.MainMenuController()
    controller()


if __name__ == "__main__":
    main()


"""
from controllers import base_controller



def main():


    instance_first_title = FirstTitles()
    print(instance_first_title)
    instance = base_controller.MainMenuController()
    menu = Menu()
    instance.menu_display(menu.main_menu)
    base_controller.PlayerController_Menu()
    base_controller.TournoiController_Menu()



if __name__ == '__main__':
    main()


"""
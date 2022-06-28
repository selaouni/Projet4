#from controllers import (player_controller, tournoi_controller)


class FirstTitles:

    def Titles(self):
        print("-------------------- Bienvenue - Tournoi d'échecs --------------------")
        print("-" * 70)
        print("-" * 70)
        print("-----------------------Menu principal---------------------------------")
        print("-" * 70)


class Menu:

    main_menu = [("1", "Créer un nouveau joueur"),
                    ("2", "Mettre à jour un joueur"),
                    ("3", "Créer un nouveau tournoi"),
                    ("4","Reprendre un tournoi"),
                    ("5", "Rapport"),]



    report_menu = [("1",  "Afficher les tournois"),
                   ("2", "Afficher les joueurs par ordre alphabétique"),
                   ("3", "Afficher les tours"),
                   ("4", "Afficher les matchs"),
                   ("5", "Afficher les joueurs selon leurs classements"),]

#   def __init__(self):
#        self.create_player = player_controller.CreatePlayerController()
#        self.create_tournoi = tournoi_controller.CreateTournoiController()


    def __call__(self, menu):
        for i in menu:
            print(" - " + i[0] + " - " + i[1])
        while True:
            data = input("Saisir le chiffre correspondant au menu souhaité : ")
            for line in menu:
                if data == line[0]:
                    return str(line[0])


            print("Erreur ! Merci de saisir l'un des chiffres affichés")




"""
print ("--------------------------------------------------------------------------------------------------------")
x = Menu()
print(x.main_menu)
print(x.report_menu)
print("*"*50)
y = x.__call__(x.report_menu)

print(y)

print ("--------------------------------------------------------------------------------------------------------")



print ("--------------------------------------------------------------------------------------------------------")



print ("--------------------------------------------------------------------------------------------------------")
Instance_main_menu = MainMenu.main_menu
print(Instance_main_menu)
print ("--------------------------------------------------------------------------------------------------------")
Instance_player_menu = MainMenu.player_menu
print (Instance_player_menu)
Instance_tournoi_menu = MainMenu.tournoi_menu
print ("--------------------------------------------------------------------------------------------------------")
print (Instance_tournoi_menu)
Instance_tournoi_report = MainMenu.tournoi_report_menu
print ("--------------------------------------------------------------------------------------------------------")
print(Instance_tournoi_report)
print ("--------------------------------------------------------------------------------------------------------")

main_menu = [("1", "Menu principal Joueur"),
                ("2", "Menu principal Tournoi"),
                ("3", "Quitter")]
                 
                 
main_menu = [("1", "Créer un joueur"),
                ("2", "Mettre à jour le classement d'un joueur"),
                ("3", "Retour au menu principal")]                 
"""

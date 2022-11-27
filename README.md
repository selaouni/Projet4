# Openclassrooms / Projet4 - parcours "Developpeur d'application python"

Date: Septembre 2022 


## Titre du projet:  
Développez un programme logiciel en Python

## Mentor:
Idriss Benjeloun

## Contributeur:    
Sabah ELAOUNI    

## Description:   

Il s'agit d'un programme qui permet de gérer des tournois d'echecs, selon le context suivant:

- le programme est lancé hors ligne depuis la console
- le programme est developpé en Python et utilise la programmation orientée objet
- l'architecture utlisée est le modèle MVC (Modele, Vue, Controleur)
- le module Tinydb a été utilisé pour gérer la base de données
- la Flake8 a été utilisée pour le peluchage du code


Les spécifications techniques sont comme suit:

- DÉROULEMENT DE BASE DU TOURNOI:
    1. Création d'un nouveau tournoi.
    2. Ajout de  huit joueurs.
    3. Géneration des paires de joueurs pour le premier tour.
    4. saisie les résultats une fois le tour est terminé.
    5. Répétition des étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, 
       et que le tournoi soit terminé.
 
- GÉNÉRATION DES PAIRES DE JOUEURS : les paires de jouzurs sont générées selon le système de tournoi suisse.

- MENU PRINCIPAL DU PROJET: 
  
  ----------------------- Menu principal -------------------------------
  ----------------------------------------------------------------------
 - 1 - Créer un nouveau joueur
 - 2 - Mettre à jour un joueur
 - 3 - Créer un nouveau tournoi
 - 4 - Reprendre un tournoi
 - 5 - Rapport joueurs
 - 6 - Rapport tournoi
 - 7 - Quitter

  
## Exécution du programme  
 

    - Créez et activez l'environnement virtuel à l'aide de la commande:
        >> pip install venv
    - Installez les modules necessaires à l'aide du fichier requirement.txt en utilisant la commande:   
        >> pip install -r requirements.txt  
    - Créer un dossier projet sur votre machine comme repository local
    - Clonner le repo distant dans votre repository local  
    - Executez le programme à partir de main.py et suivez les instructions du menu ou en utilisant la commande:
        >> python main.py
    -> Nota:l'IDE utilisé pour ce projet : PYCHARM 2022.2.1 (Community Edition)

  
## Rapport Flake8:    
  Le rapport Flak 8 de ce projet se trouve dans le repertoire flake-rapport , pour générer un nouveau rapport Flak 8:

    - Installer le module flake8 avec la commande:   
       >> python -m pip install flake8
    - installer flake8-html avec la commande:
       >> python pip install flake8-html  
    - Génerer les rapports avec: 
       >> flake8 --format=html --htmldir=flake-report
    - Generation du rapport en excluant "env" de l'analyse:
       >> flake8 --format=html --htmldir=flake-report --exclude=./env
    - pour génerer le rapport dans le terminal d'un fichier.py spécifique vous pouvez utiliser la commande:
       >>  flake8 fichier.py ou flake8 dossier/fichier.py

  Le fichier .flak8 à la racine contient la configuration optée pour la génération du rapport.


## Historique des Versions:    

 *Principales versions sous Github*
 - Flak8 and PEP8 verification 15/09/2022
 - Code update + adjustment of the MVC model + save datas correctly into DB - 14/09/2022
 - Code update (add, sort , split players, make matchs) - 05/09/2022 
 - Add the TinyDB tables (players & tournoi) - 06/07/2022
 - Basic Controller , player & tournament controller Adjustment - 30/06/2022 
 - Basic Controller and models Adjustment - 29/06/2022 
 - Update main.py - 28/06/2022 
 - First vesrion with the MVC model - 28/06/2022


## Acknowledgments (code inspiration): 

- https://www.giacomodebidda.com/posts/mvc-pattern-in-python-introduction-and-basicmodel/
- https://stackoverflow.com/questions/40827356/find-a-value-in-json-using-python
- https://www.honeybadger.io/blog/python-instantiation-metaclass
- https://www.freecodecamp.org/news/get-started-with-tinydb-in-python/
- https://www.skillsugar.com/how-to-count-the-number-of-for-loop-iterations-in-python
- https://datatofish.com/sort-pandas-dataframe/
- https://pypi.org/project/flake8-html/
- https://edk2-docs.gitbook.io/edk-ii-python-development-process-specification/environment_setup_and_example/2_create_project_configuration_file_for_flake8
- Discord DA python

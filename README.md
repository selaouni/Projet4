# Openclassrooms / Projet4 - parcours "Developpeur d'application python"

Date: Septembre 2022 


## Titre du projet:  
Développez un programme logiciel en Python

## Mentor:
Idriss Benjeloun

## Contributeur:    
    - Sabah ELAOUNI    

## Description:   

Il s'agit d'un programme qui permet de gérer des tournois d'echecs, selon le context suivant:

- le programme est lancé hors ligne depuis la console
- le programme est developpé en Python en utilisant la programmation orientée objet
- l'architecture utlisée est le modèle MVC (Modele, Vue, Controleur)
- le module tinydb a été utilisé pour gérer la base de données
- la flake8 a été utilisée pour le peluchage du code


Les spécifications techniques sont comme suit:

- DÉROULEMENT DE BASE DU TOURNOI:
    1. Créer un nouveau tournoi.
    2. Ajouter huit joueurs.
    3. Géneration des paires de joueurs pour le premier tour.
    4. Lorsque le tour est terminé saisir les résultats.
    5. Répétition des étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.
 
- GÉNÉRATION DES PAIRES DE JOUEURS : paires sont générées selon le système de tournoi suisse.
  - Menu principal du programme: 
    ----------------------- Menu principal ---------------------------------
    ------------------------------------------------------------------------
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

  
## Rapport flake8:    
  Le rapport Flak 8 de ce projet se trouve dans le repertoire flake-rapport , pour générer un nouveau rapport Flak 8:

    - Installer le module flake8 avec la commande:   
       >> python -m pip install flake8
    - installer flake8-html avec la commande:
       >> python pip install flake8-html  
    - Génerer les rapports avec: 
       >> flake8 --format=html --htmldir=flake-report
    
  
     

## Historique des Versions:    
 *Principales versions sous Github*
 - Final 
 - Optimized 
 - First 

## Acknowledgments (code inspiration): 

- https://stackoverflow.com/questions/40827356/find-a-value-in-json-using-python
- https://www.freecodecamp.org/news/get-started-with-tinydb-in-python/
- https://datatofish.com/sort-pandas-dataframe/
- https://pypi.org/project/flake8-html/
- Discord DA python
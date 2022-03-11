# Projet 11 : Améliorez une application Web Python par des tests et du débogage.
## gudlift-registration
&nbsp;
&nbsp;

L'application permet à des clubs de réserver des places pour participer à des compétitions.

Fonctionnalités principales:

Le secrétaire d'un club peut:
- se connecter à l'application (identification par email)
- visualiser le nombre de points disponibles pour son club.
- sélectionner une compétition à venir.
- échanger des points contre des places pour participer à cette compétition.

&nbsp;
&nbsp;
># Installation
1. Créer un dossier pour l'application

2. Dans ce dossier, créer un environnement virtuel avec la commande:
- sous Windows: `python -m venv <environment_name>`  
- sous Linux: `python3 -m venv <environment_name>`

3. Activer cet environnement avec la commande:
- sous Windows: `<environment_name>\Scripts\Activate.ps1`
- sous Linux: `source <environment_name>/bin/activate`

4. Télecharger (puis décompresser) l'application depuis le repository github branche QA

5. Installer la liste des paquets Python nécessaires dans cet environnement avec la commande:
- sous Windows: `pip install -r requirements.txt`
- sous Linux: `pip3 install -r requirements.txt`  

&nbsp;
># Exécution de l'application
Pour lancer le programme, taper la commande: `flask run`

&nbsp;
># Exécution des tests
Pour exécuter les tests, taper la commande: `pytest`

&nbsp;
># Taux de couverture des tests
- Pour afficher le taux de couverture des tests, taper la commande: `pytest --cov=.`
- Pour obtenir le rapport du taux de couverture des tests au format html, taper la commande: `coverage html`
- Le rapport du taux de couverture des tests est disponible au format html:
htmlcov\index.html



from bs4 import BeautifulSoup
import server


def load_the_test_database(list_competitions_for_test, list_clubs_for_test):
    """ chargement de données pour les tests (clubs et compétitions) """
    server.clubs = list_clubs_for_test["clubs"]
    server.competitions = list_competitions_for_test["competitions"]


def get_message_flash(response, category):
    """ retourne les message d'alert flash """
    return BeautifulSoup(response.data, "lxml").find('div', {'class': 'alert alert-' + category}).text

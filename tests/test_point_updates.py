
from bs4 import BeautifulSoup
from tests import utils


def test_point_updates(client, list_competitions_for_test, list_clubs_for_test):
    """ Teste la mise à jour du nombre de points disponibles pour le club. """
    PLACES_REQUESTED = 6
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/purchasePlaces', data={'competition': "Competition name 1",
                                                    'club': "club name1",
                                                    'places': PLACES_REQUESTED})
    assert get_points_available(response) == '12'


def test_point_updates_equal_zero(client, list_competitions_for_test, list_clubs_for_test):
    """ Teste la possibilité d'utiliser tous les points disponibles d'un club. """
    PLACES_REQUESTED = 4
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/purchasePlaces', data={'competition': "Competition name 1",
                                                    'club': "club name2",
                                                    'places': PLACES_REQUESTED})
    assert get_points_available(response) == '0'


def test_contest_is_complete(client, list_competitions_for_test, list_clubs_for_test):
    """
    Lorsque le concours est complet, le lien 'Book Places'
    est remplacé par le message 'This contest is full'
    """
    PLACES_REQUESTED = 5
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/purchasePlaces', data={'competition': "Competition name 3",
                                                    'club': "club name1",
                                                    'places': PLACES_REQUESTED})
    assert get_message(response=response, competition_number=2) == 'This contest is full'


def get_message(response, competition_number):
    return BeautifulSoup(response.data, "lxml").findAll('li')[competition_number].find('span').text


def get_points_available(response):
    return BeautifulSoup(response.data, "lxml").find('div', {'class': 'col'}).text[-2:].strip()

from pickle import TRUE
from bs4 import BeautifulSoup
from tests import utils
import utilities


def test_past_competition(client, list_competitions_for_test, list_clubs_for_test):
    """
    Lorsque la date de la compétition est passée, le lien 'Book Places' est remplacé par
    le message 'Past competition'
    """
    email = 'club1@club.com'
    utilities.ACTUAL_DATE_TODAY = True
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    if not get_link_to_book(response=response, competition_number=0):
        assert TRUE
    assert get_message(response=response, competition_number=0) == 'Past competition'


def test_upcoming_competition(client, list_competitions_for_test, list_clubs_for_test):
    """ Lorsque la date de la compétition est à venir, le lien 'Book Places' apparait sur la page """
    email = 'club1@club.com'
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert get_link_to_book(response=response, competition_number=1).text == 'Book Places'


def get_link_to_book(response, competition_number):
    return BeautifulSoup(response.data, "lxml").findAll('li')[competition_number].find('a')


def get_message(response, competition_number):
    return BeautifulSoup(response.data, "lxml").findAll('li')[competition_number].find('span').text


from tests import utils
from bs4 import BeautifulSoup


def test_valid_email(client, list_clubs_for_test, list_competitions_for_test):
    """ La saisie d'un mail valide (présent dans les données des clubs) permet de se connecter. """
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    email = 'club1@club.com'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert get_message_welcome(response) == 'Welcome, club1@club.com'


def test_unvalid_email(client, list_clubs_for_test, list_competitions_for_test):
    """ La saisie d'un mail non valide (non présent dans les données des clubs),
    provoque l'affichage du message: "Sorry, that email wasn't found.". """
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    email = 'a@a.com'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Sorry, that email wasn't found."


def test_email_field_empty(client, list_clubs_for_test, list_competitions_for_test):
    """ Si le champ 'email' reste vide, alors le message: "Sorry, that email wasn't found." s'affiche. """
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    email = ''
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Sorry, that email wasn't found."


def test_not_a_email(client, list_clubs_for_test, list_competitions_for_test):
    """ Si le champ 'email' est complété avec une chaine de caratère quelconque,
    alors le message: "Sorry, that email wasn't found." s'affiche. """
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    email = 'oc'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Sorry, that email wasn't found."


def test_email_unicity(client, invalid_datas_clubs_for_test, list_competitions_for_test):
    """ S'il existe plusieurs clubs avec le même email alors le message "Email must be unique." s'affiche. """
    utils.load_the_test_database(list_competitions_for_test, invalid_datas_clubs_for_test)
    email = 'club1@club.com'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Email must be unique."


def get_message_welcome(response):
    return BeautifulSoup(response.data, "lxml").find('h2').text.strip()

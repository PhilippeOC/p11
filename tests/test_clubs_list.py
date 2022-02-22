from bs4 import BeautifulSoup
import server
from tests import utils


def test_club_list(client, list_clubs_for_test):
    """ Teste l'affichage de la liste des clubs (nom et points)
    si l'utilisateur est connecté. """
    server.clubs = list_clubs_for_test["clubs"]
    email = 'club1@club.com'
    client.post('/showSummary', data={'email': email})
    response = client.get(f'/listClubsPoints/{email}')
    list_clubs = BeautifulSoup(response.data, "lxml").findAll('li')
    for i, club in enumerate(list_clubs):
        club_name_point = (f"Club: {list_clubs_for_test['clubs'][i]['name']} --- "
                           f"Points: {list_clubs_for_test['clubs'][i]['points']}")
        assert club.text.strip() == club_name_point
    assert response.status_code == 200


def test_unauthorized_access_to_club_list(client):
    """ Teste qu'un utilisateur non connecté ne puisse pas accèder à la liste des clubs,
    et qu'il est redirigé vers la page d'accueil. """
    response = client.get('/listClubsPoints/oc')
    assert response.status_code == 200
    assert utils.get_message_welcome_page(response) == 'Welcome to the GUDLFT Registration Portal!'

from bs4 import BeautifulSoup
import server


def test_club_list(client, list_clubs_for_test):
    """ Teste l'affichage de la liste des clubs (nom et points)
    sur la page d'accueil du site. """
    server.clubs = list_clubs_for_test["clubs"]
    response = client.get('/')
    list_clubs = BeautifulSoup(response.data, "lxml").findAll('li')
    for i, club in enumerate(list_clubs):
        club_name_point = (f"Club: {list_clubs_for_test['clubs'][i]['name']} --- "
                           f"Points: {list_clubs_for_test['clubs'][i]['points']}")
        assert club.text.strip() == club_name_point
    assert response.status_code == 200

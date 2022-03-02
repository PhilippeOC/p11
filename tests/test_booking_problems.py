from tests import utils


def test_not_found_club(client, list_competitions_for_test, list_clubs_for_test):
    """
    Teste si le message d'alerte 'Something went wrong-please try again' s'affiche
    si le club n'est pas trouvé lors de la reservation de places.
    """
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    client.post('/showSummary', data={'email': 'club1@club.com'})
    competition = list_competitions_for_test['competitions'][0]
    club = {"name": "doesn't exist"}
    response = client.get(f"book/{competition['name']}/{club['name']}")
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Something went wrong-please try again"


def test_not_found_competition(client, list_competitions_for_test, list_clubs_for_test):
    """
    Teste si le message d'alerte 'Something went wrong-please try again' s'affiche
    si la compétition n'est pas trouvée lors de la reservation de places.
    """
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    client.post('/showSummary', data={'email': 'club1@club.com'})
    competition = {"name": "doesn't exist"}
    club = list_clubs_for_test['clubs'][0]
    response = client.get(f"book/{competition['name']}/{club['name']}")
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Something went wrong-please try again"


def test_find_several_clubs_with_the_same_name(client,
                                               list_competitions_for_test,
                                               invalid_datas_clubs_for_test):
    """
    Teste si le message d'alerte 'Something went wrong-please try again' s'affiche
    si plusieurs clubs trouvés ont le même nom lors de la reservation de places.
    """
    utils.load_the_test_database(list_competitions_for_test, invalid_datas_clubs_for_test)
    client.post('/showSummary', data={'email': 'club2@club.com'})
    competition = list_competitions_for_test['competitions'][0]
    club = {"name": "club name1"}
    response = client.get(f"book/{competition['name']}/{club['name']}")
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Something went wrong-please try again"


def test_find_several_competitions_with_the_same_name(client,
                                                      invalid_datas_competitions_for_test,
                                                      list_clubs_for_test):
    """
    Teste si le message d'alerte 'Something went wrong-please try again' s'affiche
    si plusieurs compétitions trouvées ont le même nom lors de la reservation de places.
    """
    utils.load_the_test_database(invalid_datas_competitions_for_test, list_clubs_for_test)
    client.post('/showSummary', data={'email': 'club1@club.com'})
    competition = {"name": "Competition name 1"}
    club = list_clubs_for_test['clubs'][0]
    response = client.get(f"book/{competition['name']}/{club['name']}")
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "Something went wrong-please try again"


def test_unauthorized_access_to_the_booking_page(client):
    """ Teste qu'un utilisateur non connecté ne puisse pas accéder à la page des réservations,
    et qu'il est redirigé vers la page d'accueil."""
    response = client.get("book/Competition name 1/club name1")
    assert response.status_code == 200
    assert utils.get_message_welcome_page(response) == 'Welcome to the GUDLFT Registration Portal!'

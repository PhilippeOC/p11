from tests import utils


def test_places_requested_less_than_12(client, list_competitions_for_test, list_clubs_for_test):
    """ Si la demande de réservation est de moins de 12 places elle est effectuée et
    le message 'Great-booking complete!' s'affiche. """
    PLACES_REQUESTED = 9
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/purchasePlaces', data={'competition': "Competition name 1",
                                                    'club': "club name1",
                                                    'places': PLACES_REQUESTED})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'success') == 'Great-booking complete!'


def test_places_requested_more_than_12(client, list_competitions_for_test, list_clubs_for_test):
    """ Si la demande de réservation est de plus de 12 places elle n'est pas effectuée et
    le message d'alert 'You can't request more than 12 places.' s'affiche. """
    PLACES_REQUESTED = 20
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/purchasePlaces', data={'competition': "Competition name 1",
                                                    'club': "club name1",
                                                    'places': PLACES_REQUESTED})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "You can't request more than 12 places."

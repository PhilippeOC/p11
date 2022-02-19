from tests import utils


def test_less_points_than_allowed(client, list_competitions_for_test, list_clubs_for_test):
    """ Lors de la réservation, si la demande du nombre de places est inférieure au nombre de points disponibles,
    alors le message 'Great-booking complete!' s'affiche. """
    PLACES_REQUESTED = 6
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/purchasePlaces', data={'competition': "Competition name 1",
                                                    'club': "club name1",
                                                    'places': PLACES_REQUESTED})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'success') == 'Great-booking complete!'


def test_more_points_than_allowed(client, list_competitions_for_test, list_clubs_for_test):
    """ Lors de la réservation, si la demande du nombre de places est supérieure au nombre de points disponibles,
    alors le message 'You can't redeem more points than available.' s'affiche. """
    PLACES_REQUESTED = 5
    utils.load_the_test_database(list_competitions_for_test, list_clubs_for_test)
    response = client.post('/purchasePlaces', data={'competition': "Competition name 1",
                                                    'club': "club name2",
                                                    'places': PLACES_REQUESTED})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "You can't redeem more points than available."

from tests import utils


def test_buy_a_negative_number_of_places(client):
    """ Si l'utilisateur entre une valeur négative dans le champ 'How many places?'
        le message d'alerte "The number of places must be strictly positive" s'affiche.
    """
    response = client.post('/purchasePlaces', data={'competition': "Competition name 1",
                                                    'club': "club name1",
                                                    'places': -2})
    assert response.status_code == 200
    assert utils.get_message_flash(response, 'danger') == "The number of places must be strictly positive"

import pytest

import server


@pytest.fixture
def client():
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def list_clubs_for_test():
    return {"clubs": [
                        {
                            "name": "club name1",
                            "email": "club1@club.com",
                            "points": "13"
                        },
                        {
                            "name": "club name2",
                            "email": "club2@club.com",
                            "points": "4"
                        },
                        {
                            "name": "club name3",
                            "email": "club3@club.com",
                            "points": "12"
                        }
                    ]}


@pytest.fixture
def list_competitions_for_test():
    return {"competitions": [
                    {
                        "name": "Competition name 1",
                        "date": "2020-03-27 10:00:00",
                        "numberOfPlaces": "25"
                    },
                    {
                        "name": "Competition name 2",
                        "date": "2025-10-22 13:30:00",
                        "numberOfPlaces": "13"
                    },
                    {
                        "name": "Competition name 3",
                        "date": "2028-10-22 13:30:00",
                        "numberOfPlaces": "0"
                    }
                ]}


@pytest.fixture
def invalid_datas_clubs_for_test():
    return {"clubs": [
                        {
                            "name": "club name1",
                            "email": "club1@club.com",
                            "points": "13"
                        },
                        {
                            "name": "club name1",
                            "email": "club2@club.com",
                            "points": "4"
                        },
                        {
                            "name": "club name3",
                            "email": "club1@club.com",
                            "points": "12"
                        }
                    ]}

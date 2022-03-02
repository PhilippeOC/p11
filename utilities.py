import json
from flask import render_template

from datetime import datetime
from constants import ACTUAL_DATE_TODAY


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


def render_template_booking(competition, club):
    return render_template('booking.html',
                           title=f"Booking for {competition['name']} || GUDLFT",
                           competition=competition,
                           club=club)


def render_template_welcome(competitions, club):
    return render_template('welcome.html',
                           title="Summary | GUDLFT Registration",
                           club=club,
                           competitions=competitions)


def check_valid_date(competition):
    """
        competition['valid_date'] = True si la date de la compétition est à venir
        Pour tester l'IHM, si ACTUAL_DATE_TODAY est fixée à False (voir constant.py),
        une date antérieure à la date actuelle est utilisée.
    """
    today = datetime.now() if ACTUAL_DATE_TODAY else datetime.strptime("2010-04-27 10:00:00", '%Y-%m-%d %H:%M:%S')
    competition_date = datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S')
    competition['valid_date'] = today < competition_date


def find_one(item, items):
    """ retourne item si cet item est unique dans items
    sinon retourne False """
    found_item = [c for c in items if c['name'] == item]
    return found_item[0] if len(found_item) == 1 else False

import json
from flask import render_template


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

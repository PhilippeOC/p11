from flask import Flask, render_template, request, redirect, flash, url_for, session

from constants import PROPORTION_PLACES_POINTS, PLACES_MAX
from utilities import (load_clubs,
                       load_competitions,
                       render_template_booking,
                       render_template_welcome,
                       check_valid_date,
                       find_one)

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    return render_template('index.html', title="GUDLFT Registration")


@app.route('/showSummary', methods=['POST'])
def show_summary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    if club:
        if len(club) > 1:
            flash("Email must be unique.", 'danger')
            return render_template('index.html')
        club = club[0]
        session['email'] = request.form['email']
        for competition in competitions:
            check_valid_date(competition)
        return render_template_welcome(competitions, club)
    flash("Sorry, that email wasn't found.", "danger")
    return render_template('index.html', title="GUDLFT Registration")


@app.route('/book/<competition>/<club>')
def book(competition, club):
    if 'email' not in session:
        return render_template('index.html', title="GUDLFT Registration")

    found_club = find_one(club, clubs)
    found_competition = find_one(competition, competitions)

    if found_club and found_competition:
        return render_template_booking(found_competition, found_club)

    flash("Something went wrong-please try again", "danger")
    return render_template_welcome(competitions, club)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    number_of_places = int(competition['numberOfPlaces'])
    if places_required <= 0:
        flash("The number of places must be strictly positive", 'danger')
        return render_template_booking(competition, club)

    if places_required > PLACES_MAX:
        flash(f"You can't request more than {PLACES_MAX} places.", 'danger')
        return render_template_booking(competition, club)

    if number_of_places <= 0:
        return render_template_welcome(competitions, club)
    number_of_places_available = number_of_places-places_required
    points_available = int(club['points']) - places_required * PROPORTION_PLACES_POINTS

    if number_of_places_available >= 0 and points_available >= 0:
        competition['numberOfPlaces'] = number_of_places_available
        club['points'] = points_available
        flash('Great-booking complete!', 'success')
        return render_template_welcome(competitions, club)

    flash("You can't redeem more points than available.", 'danger')
    return render_template_booking(competition, club)


@app.route('/listClubsPoints/<email>')
def list_clubs_points(email):
    if 'email' not in session:
        return render_template('index.html', title="GUDLFT Registration")
    return render_template('listClubs.html', clubs=clubs, email=email, title='List of clubs')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

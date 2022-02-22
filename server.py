from flask import Flask, render_template, request, redirect, flash, url_for, session

from constants import PROPORTION_PLACES_POINTS, PLACES_MAX
from utilities import loadClubs, loadCompetitions, render_template_booking, render_template_welcome, check_valid_date

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html', title="GUDLFT Registration")


@app.route('/showSummary', methods=['POST'])
def showSummary():
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
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template_booking(foundCompetition, foundClub)
    else:
        flash("Something went wrong-please try again", "danger")
        return render_template_welcome(competitions, club)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    numberOfPlaces = int(competition['numberOfPlaces'])

    if placesRequired > PLACES_MAX:
        flash(f"You can't request more than {PLACES_MAX} places.", 'danger')
        return render_template_booking(competition, club)

    if numberOfPlaces <= 0:
        return render_template_welcome(competitions, club)
    numberOfPlacesAvailable = numberOfPlaces-placesRequired
    pointsAvailable = int(club['points']) - placesRequired * PROPORTION_PLACES_POINTS

    if numberOfPlacesAvailable >= 0 and pointsAvailable >= 0:
        competition['numberOfPlaces'] = numberOfPlacesAvailable
        club['points'] = pointsAvailable
        flash('Great-booking complete!', 'success')
        return render_template_welcome(competitions, club)

    flash("You can't redeem more points than available.", 'danger')
    return render_template_booking(competition, club)


@app.route('/listClubsPoints/<email>')
def listClubsPoints(email):
    if 'email' not in session:
        return render_template('index.html', title="GUDLFT Registration")
    return render_template('listClubs.html', clubs=clubs, email=email, title='List of clubs')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

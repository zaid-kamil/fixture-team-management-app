from flask import Blueprint, Flask, redirect, render_template, request

from models.fixture import Fixture
import repositories.fixture_repository as fixture_repository
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

fixtures_blueprint = Blueprint("fixtures", __name__)

# INDEX
@fixtures_blueprint.route("/fixtures")
def fixtures():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()
    return render_template("fixtures/index.html", all_fixtures=fixtures, teams=teams)


# NEW
# GET '/fixtures/new' --> show an html form to create a new fixture
@fixtures_blueprint.route("/fixtures/new")
def new_fixture():
    teams = team_repository.select_all()
    return render_template("fixtures/new.html", teams=teams)    

# CREATE
# POST '/fixtures' --> handle the post from the new form
@fixtures_blueprint.route("/fixtures", methods=["POST"])
def create_fixture():
    team1 = request.form["team1"]
    team2 = request.form["team2"]
    fixture = Fixture(team1, team2, id)
    if (fixture.team1 == fixture.team2):
        return redirect("/fixtures")
    else:
        fixture_repository.save(fixture)
        return redirect("/fixtures")


# SHOW
# GET '/fixtures/<id>' --> show some html for a specific fixture
@fixtures_blueprint.route("/fixtures/<id>")
def show_fixture(id):
    fixture = fixture_repository.select(id)
    return render_template("fixtures/index.html", fixture=fixture)


# EDIT
# GET '/fixtures/<id>/edit' --> show some html form to edit a specific fixture
@fixtures_blueprint.route("/fixtures/<id>/edit")
def edit_team(id):
    fixture = fixture_repository.select(id)
    teams = team_repository.select_all()
    return render_template('fixtures/edit.html', fixture=fixture, teams=teams)

# UPDATE
# PUT '/fixtures/<id>' --> handle the PUT from the edit form
@fixtures_blueprint.route("/fixtures/<id>", methods=["POST"])
def update_team(id):
    team1 = request.form["team1"]
    team2 = request.form["team2"]
    # team1.score = request.form["fixture.team1.score"]
    # team2.score = request.form["fixture.team2.score"]
    
    fixture = Fixture(team1, team2, id)
    fixture_repository.update(fixture)
    return redirect("/fixtures")

# DELETE
# DELETE '/clubs/players/<id>' --> handle the delete - to delete a specific task we
@fixtures_blueprint.route("/fixtures/<id>/delete", methods=["POST"])
def delete_fixture(id):
    fixture_repository.delete(id)
    return redirect("/fixtures")


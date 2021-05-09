from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository


teams_blueprint = Blueprint("teams", __name__)

# INDEX
@teams_blueprint.route("/clubs")
def teams():
    teams = team_repository.select_all()
    return render_template("clubs/index.html", teams=teams)


# NEW
# GET '/clubs/new' --> show an html form to create a new club
@teams_blueprint.route("/clubs/new")
def new_team():
    teams = team_repository.select_all()
    return render_template("clubs/new.html", teams=teams)    


# CREATE
# POST '/clubs' --> handle the post from the new form
@teams_blueprint.route("/clubs", methods=["POST"])
def create_team():
    new_team = Team(team_name = request.form["team_name"],
    location = request.form["location"],
    stadium_name = request.form["stadium_name"],
    stadium_capacity = request.form["stadium_capacity"],
    fixtures_played = request.form["fixtures_played"],
    fixtures_won = request.form["fixtures_won"],
    fixtures_drawn = request.form["fixtures_drawn"],
    fixtures_lost = request.form["fixtures_lost"],
    points = request.form["points"],
    score = request.form["score"])
    team_repository.save(new_team)
    return redirect("/clubs")


# SHOW
# GET '/clubs/<id>' --> show some html for a specific club
@teams_blueprint.route("/clubs/<id>")
def show_team(id):
    team = team_repository.select(id)
    teams = team_repository.select_all()
    fixtures = fixture_repository.select_all()
    return render_template("clubs/show.html", team=team, teams=teams, fixtures=fixtures)


# EDIT
# GET '/clubs/<id>/edit' --> show some html form to edit a specific club
@teams_blueprint.route("/clubs/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    teams = team_repository.select_all()
    return render_template('clubs/edit.html', team=team, teams=teams)


# UPDATE
# PUT '/clubs/<id>' --> handle the PUT from the edit form
@teams_blueprint.route("/clubs/<id>", methods=["POST"])
def update_team(id):
    team_name = request.form["team_name"]
    location = request.form["location"]
    stadium_name = request.form["stadium_name"]
    stadium_capacity = request.form["stadium_capacity"]
    fixtures_played = request.form["fixtures_played"]
    fixtures_won = request.form["fixtures_won"]
    fixtures_drawn = request.form["fixtures_drawn"]
    fixtures_lost = request.form["fixtures_lost"]
    points = request.form["points"]
    score = request.form["score"]
    
    team = Team(team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score, id)
    team_repository.update(team)
    return redirect("/clubs")


# DELETE
# DELETE '/clubs/<id>' --> handle the delete - to delete a specific task we can't use HTTP DELETE as HTML forms don't do DELETE
@teams_blueprint.route("/clubs/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/clubs")

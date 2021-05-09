from db.run_sql import run_sql
from models.player import Player
from models.team import Team

# add new team to database
def save(team):
    sql = "INSERT INTO teams (team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = [team.team_name, team.location, team.stadium_name, team.stadium_capacity, team.fixtures_played, team.fixtures_won, team.fixtures_drawn, team.fixtures_lost, team.points, team.score]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id

# get all teams from database
def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["team_name"], result["location"], result["stadium_name"], result["stadium_capacity"], result["fixtures_played"], result["fixtures_won"], result["fixtures_drawn"], result["fixtures_lost"], result["points"], result["score"], result["id"])
        teams.append(team)
    return teams


# get specific team from database
def select(id):
    sql = "SELECT * FROM teams WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]
    team = Team(result["team_name"], result["location"], result["stadium_name"], result["stadium_capacity"], result["fixtures_played"], result["fixtures_won"], result["fixtures_drawn"], result["fixtures_lost"], result["points"], result["score"], result["id"])
    return team


# update specific fixture in database
def update(team):
    sql = "UPDATE teams SET (team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score) = (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [team.team_name, team.location, team.stadium_name, team.stadium_capacity, team.fixtures_played, team.fixtures_won, team.fixtures_drawn, team.fixtures_lost, team.points, team.score, team.id]
    run_sql(sql, values)


# delete all
def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)


#delete specific entry
def delete(id):
    sql = "DELETE FROM teams WHERE id = ?"
    values = [id]
    run_sql(sql, values)
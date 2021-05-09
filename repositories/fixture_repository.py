from db.run_sql import run_sql
from models.fixture import Fixture
from models.player import Player
import repositories.player_repository as player_repository
from models.team import Team
import repositories.team_repository as team_repository

# add new fixture to database
def save(fixture):
    sql = "INSERT INTO fixtures (team1_id, team2_id) VALUES (%s, %s) RETURNING id"
    values = [fixture.team1, fixture.team2]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id
    return fixture

# get all fixtures from database
def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)
    for result in results:
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        fixture = Fixture(team1, team2, result["id"])
        fixtures.append(fixture)
    return fixtures

# get specific fixture from database
def select(id):
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    fixture = Fixture(result["team1_id"], result["team2_id"], result["id"])
    return fixture

# update specific fixture in database
def update(fixture):
    sql = "UPDATE fixtures SET (team1_id, team2_id) = (%s, %s) WHERE id = %s"
    values = [fixture.team1, fixture.team2, fixture.id]
    run_sql(sql, values)

# delete all
def delete_all():
    sql = "DELETE FROM fixtures"
    run_sql(sql)

#delete specific entry
def delete(id):
    sql = "DELETE FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)

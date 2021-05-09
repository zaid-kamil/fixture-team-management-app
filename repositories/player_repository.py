from db.run_sql import run_sql
from models.player import Player

# add new player to database
def save(player):
    sql = "INSERT INTO players (name, player_info, goals_scored) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.player_info, player.goals_scored]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player


# get all players from database
def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Player(result["name"], result["player_info"], result["goals_scored"], result["id"])
        players.append(player)
    return players


# get specific player from database
def select(id):
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    player = Player(result["name"], result["player_info"], result["goals_scored"], result["id"])
    return player


# update specific player in database
def update(player):
    sql = "UPDATE players SET (name, player_info, goals_scored) = (%s, %s, %s) WHERE id = %s"
    values = [player.name, player.player_info, player.goals_scored, player.id]
    run_sql(sql, values)


# delete all
def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)


#delete specific entry
def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)
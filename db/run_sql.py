import sqlite3

def run_sql(sql, values = None):
    results = []
    conn = None
    try:
        conn = sqlite3.connect("fixture.db")
        if values:
            conn.execute(sql, values)
        else:
            conn.execute(sql)
        conn.commit()
        results = conn.cursor().fetchall()
        conn.close()
        print("[>] Query executed\n",sql)
    except (Exception, sqlite3.DatabaseError) as error:
        print("[x] in query\n",sql)
        print("[x] values\n",values)
        print("[x]",error)
    finally:
        if conn is not None:
            conn.close()
    return results


if __name__ == '__main__':
    run_sql("""
    CREATE TABLE teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name VARCHAR(255),
    location VARCHAR(255),
    stadium_name VARCHAR(255),
    stadium_capacity INTEGER,
    fixtures_played INTEGER,
    fixtures_won INTEGER,
    fixtures_drawn INTEGER,
    fixtures_lost INTEGER,
    points INTEGER,
    score INTEGER);
    """)
    run_sql("""
    CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    player_info VARCHAR(255),
    goals_scored INTEGER);
    """)

    run_sql("""
    CREATE TABLE fixtures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team1_id INTEGER, 
    team2_id INTEGER, 
    FOREIGN KEY(team2_id) REFERENCES teams(id) ON DELETE CASCADE,
    FOREIGN KEY(team1_id) REFERENCES teams(id) ON DELETE CASCADE);
    """)
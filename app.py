from flask import Flask, render_template

from controllers.fixtures_controller import fixtures_blueprint
from controllers.players_controller import players_blueprint
from controllers.teams_controller import teams_blueprint
import repositories.team_repository as team_repository


app = Flask(__name__)

app.register_blueprint(fixtures_blueprint)
app.register_blueprint(players_blueprint)
app.register_blueprint(teams_blueprint)

@app.route("/")
def main():
    teams = team_repository.select_all()
    return render_template('index.html', teams=teams)


@app.route("/tables")
def tables():
    teams = team_repository.select_all()
    return render_template('tables/index.html', teams=teams)

if __name__ == '__main__':
    app.run()

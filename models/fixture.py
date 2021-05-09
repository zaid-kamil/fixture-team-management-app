class Fixture:
    def __init__(self, team1, team2, id=None):
        self.team1 = team1
        self.team2 = team2
        self.id = id
# future functionality - add team scores here to allow editing in fixture (remove from team.py)

# this function sets up a fixture
    def setup_fixture(self, team1, team2):
        return "{team1.team_name}" + "v" + "{team2.team_name}"

# this function determines the winner of the fixture
    def determine_winner(self):
        if self.team1.score == self.team2.score:
            return None
        elif self.team1.score > self.team2.score:
            return self.team1.team_name
        elif self.team1.score < self.team2.score:
            return self.team2.team_name

#this function adds the points won to the team total in the table, add game played and game lost to losers stats
    def add_points(self, team1, team2):
        if (self.determine_winner ==  self.team1.team_name):
            self.team1.add_points_win()
            self.team2.update_team_stats()
# same but team 2 winner
        elif (self.determine_winner ==  self.team2.team_name):
            self.team2.add_points_win()
            self.team1.update_team_stats()
# same but for a draw
        elif self.determine_winner == None:
            self.team1.add_point_draw()
            self.team2.add_point_draw()


#this function adds the points won to the team total in the table
    # def add_points_win(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score):
        # fixture winner + 3 points for win, add game to played and won
        # points += 3
        # fixtures_played = fixtures_played + 1
        # fixtures_won = fixtures_won + 1
        

# same but for a draw
    # def add_point_draw(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score):
    #     fixtures_played = fixtures_played + 1
    #     fixtures_won = fixtures_won + 1
    #     points = points + 1

# add to fixtures_played and fixtures_lost to losers stats
    # def update_team_stats(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score):
    #     fixtures_played = fixtures_played + 1
    #     fixtures_lost = fixtures_lost + 1

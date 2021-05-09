class Team:
    def __init__(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score, id=None):
        self.team_name = team_name
        self.location = location
        self.stadium_name = stadium_name
        self.stadium_capacity = stadium_capacity
        self.fixtures_played = fixtures_played
        self.fixtures_won = fixtures_won
        self.fixtures_drawn = fixtures_drawn
        self.fixtures_lost = fixtures_lost
        self.points = points
        self.score = score   #### could remove from here and add to fixtures, would need to update logic
        self.id = id


#this function adds the points won to the team total in the table
    def add_points_win(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score):
        # fixture winner + 3 points for win, add game to played and won
        fixtures_played +=1
        fixtures_won +=1
        points += 3


# same but for a draw
    def add_point_draw(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score):
        fixtures_played +=1
        fixtures_won +=1
        points += 1


# add to fixtures_played and fixtures_lost to losers stats
    def update_team_stats(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score):
        fixtures_played += 1 
        fixtures_lost += 1
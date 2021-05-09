import unittest
from models.team import Team
from models.player import Player
from models.fixture import Fixture



class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team1 = Team("Team 1", "Edinburgh, Scotland", "Murrayfield", 67000, 4, 0, 4, 0, 4, 1)
        self.team2 = Team("Team 2", "Glasgow, Scotland", "Hampden", 52000, 4, 0, 4, 0, 4, 1)
        self.fixture = Fixture(self.team1, self.team2)

# testing that fixture has not yet taken place, no score yet submitted
#    @unittest.skip("Delete this line to run the test")
    def test_determine_fixture_played(self):
        self.assertEqual("Team 1", self.team1.team_name)
        self.assertEqual("Team 2", self.team2.team_name)
        self.assertEqual("{team1.team_name}" + "v" + "{team2.team_name}", self.fixture.setup_fixture(self.team1, self.team2))
  


# testing function to determine the winner of the fixture/match/game
#    @unittest.skip("Delete this line to run the test")
    def test_no_winner(self):
        self.assertEqual(1, self.team1.score)
        self.assertEqual(1, self.team2.score)
        self.assertEqual(None, self.fixture.determine_winner(self.team1, self.team2))

#    @unittest.skip("Delete this line to run the test")
    def test_team1_winner(self):
        self.team1 = Team("Team 1", "Edinburgh, Scotland", "Murrayfield", 67000, 4, 0, 4, 0, 4, 2)
        self.fixture = Fixture(self.team1, self.team2)
        self.assertEqual(2, self.team1.score)
        self.assertEqual(1, self.team2.score)
        self.assertEqual(self.fixture.team1.team_name, self.fixture.determine_winner(self.team1, self.team2))

#    @unittest.skip("Delete this line to run the test")
    def test_team2_winner(self):
        self.team1 = Team("Team 1", "Edinburgh, Scotland", "Murrayfield", 67000, 4, 0, 4, 0, 4, 1)
        self.team2 = Team("Team 2", "Glasgow, Scotland", "Hampden", 52000, 4, 0, 4, 0, 4, 2)
        self.fixture = Fixture(self.team1, self.team2)
        self.assertEqual(1, self.team1.score)
        self.assertEqual(2, self.team2.score)
        self.assertEqual(self.fixture.team2.team_name, self.fixture.determine_winner(self.team1, self.team2))


    # @unittest.skip("Delete this line to run the test")
    # def test_add_points_winner(self):
    #     self.team1 = Team("Team 1", "Edinburgh, Scotland", "Murrayfield", 67000, 4, 0, 4, 0, 4, 3)
    #     self.fixture = Fixture(4, self.team2)
    #     self.assertEqual(4, self.team1.points)
    #     self.assertEqual(7, self.fixture.add_points(self.team1, self.team2))
import unittest
from models.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Diego Maradona", "Squad No: 10 - Flawed genius, one of the all time greats", 600)


#    @unittest.skip("Delete this line to run the test")
    def test_player_has_name(self):
        self.assertEqual("Diego Maradona", self.player.name)

#    @unittest.skip("Delete this line to run the test")
    def test_player_has_inf(self):
        self.assertEqual("Squad No: 10 - Flawed genius, one of the all time greats", self.player.player_info)

#    @unittest.skip("Delete this line to run the test")
    def test_player_has_games_played(self):
        self.assertEqual(600, self.player.goals_scored)
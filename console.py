import pdb

from models.fixture import Fixture
import repositories.fixture_repository as fixture_repository

from models.player import Player
import repositories.player_repository as player_repository

from models.team import Team
import repositories.team_repository as team_repository

fixture_repository.delete_all()
player_repository.delete_all()
team_repository.delete_all()

player_1 = Player("Diego Armando Maradona", "Flawed genius. Mesmerised defenders as much as he mesmerised fans. The greatest player of his generation, if not all time.", 346)
player_repository.save(player_1)

player_2 = Player("Pele", "The original greatest player in the world, Guinness world record all-time top goalscorer and scorer of the probably the best ever fictional goal with his overhead kick in Escape to Victory.", 1279)
player_repository.save(player_2)

player_3 = Player("Zinedine Zidane", "Remembered for his sublime control of the football, but also the occasional lack of control of his temper...", 126)
player_repository.save(player_3)

player_4 = Player("Ronaldo (the Brazilian one!)", "O Fenômeno. But for injuries and illness, surely we would not be debating who was the greatest player of all time.", 309)
player_repository.save(player_4)

player_5 = Player("Zlatan Ibrahimovic", "As is his way, Zlatan has the best quotes about Zlatan: We usually say that you cannot become a legend before death. But I am a living legend.", 470)
player_repository.save(player_5)

team_1 = Team("Napoli", "Naples, Italy", "Stadio San Paolo", 60000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_1)

team_2 = Team("Santos", "Sao Paulo, Brazil", "Estádio Urbano Caldeira (Vila Belmiro)", 16000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_2)

team_3 = Team("Juventus", "Turin, Italy", "Juventus Stadium", 41000, 4, 0, 4, 0, 4, 2)
team_repository.save(team_3)

team_4 = Team("Barcelona", "Barcelona, Catalonia, Spain", "Camp Nou", 99000, 4, 0, 4, 0, 4, 1)
team_repository.save(team_4)

team_5 = Team("AC Milan", "Milan, Italy", "Stadio Giuseppe Meazza (San Siro)", 80000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_5)

fixture_1 = Fixture(team_1, team_2)
fixture_repository.save(fixture_1)

fixture_2 = Fixture(team_3, team_4)
fixture_repository.save(fixture_2)

fixture_3 = Fixture(team_1, team_3)
fixture_repository.save(fixture_3)

fixture_4 = Fixture(team_2, team_4)
fixture_repository.save(fixture_4)

fixture_5 = Fixture(team_1, team_4)
fixture_repository.save(fixture_5)

fixture_6 = Fixture(team_1, team_5)
fixture_repository.save(fixture_6)

fixture_7 = Fixture(team_2, team_5)
fixture_repository.save(fixture_7)

fixture_8 = Fixture(team_3, team_5)
fixture_repository.save(fixture_8)

fixture_9 = Fixture(team_4, team_5)
fixture_repository.save(fixture_9)

fixture_10 = Fixture(team_2, team_3)
fixture_repository.save(fixture_10)

pdb.set_trace()

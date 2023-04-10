import pytest
from Cars import PlayerCar

@pytest.fixture
def player():
    player_x = 250
    player_y = 400
    player = PlayerCar(player_x, player_y)
    return player

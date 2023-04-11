import pytest
from Cars import PlayerCar

@pytest.fixture
def player():
    player_x = 250
    player_y = 400
    player = PlayerCar(player_x, player_y)
    return player

def test_player_start_position(player):
    assert player.rect.center == (250, 400)

#@pytest.mark.skip(reason="This test is not implemented yet")
def test_player_move_left(player):
    player.rect.x -= 100
    assert player.rect.center == (150, 400)

def test_player_move_right(player):
    player.rect.x += 100
    assert player.rect.center == (350, 400)
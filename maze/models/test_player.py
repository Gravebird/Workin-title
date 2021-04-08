# maze.py
# Tests Player py with pytest
# Author: Jennie

import pytest
from .player import Player

@pytest.fixture
def test_player():
    return Player((0,0))

def test_attributes(test_player):
    assert hasattr(test_player, '_backpack')
    assert type(test_player._backpack) == list

    assert hasattr(test_player, 'backpack')

    test_player.backpack = "test_item"
    assert test_player._backpack == ["test_item"]

    assert hasattr(test_player, '_space')
    assert type(test_player._space) == tuple

    assert hasattr(test_player, 'space')

    test_player.space = (0,1)
    assert test_player._space == (0,1)  
# maze.py
# Tests Maze py with pytest
# Author: Jennie

import pytest
from .maze import Maze
from .player import Player

@pytest.fixture
def test_maze():
    return Maze("testmaze.txt")

def test_attributes(test_maze):
    #- tests each attribute maze to see if they exist and are the correct type
    assert hasattr(test_maze, '_map')
    assert type(test_maze._map) == list

    assert hasattr(test_maze, '_player')
    assert type(test_maze._player) == Player

    assert hasattr(test_maze, '_exit_space')
    assert type(test_maze._exit_space) == tuple

    assert hasattr(test_maze, '_empty_spaces')
    assert type(test_maze._empty_spaces) == list

    assert hasattr(test_maze, '_map')
    assert type(test_maze._map) == list

def test_find_exit(test_maze):
    assert test_maze.find_exit() == (7,13)

def test_find_random_spot(test_maze):
    assert type(test_maze.find_random_spot() ) == tuple

def test_can_move_to(test_maze):
    assert test_maze.can_move_to(1,1) == True

def test_is_exit(test_maze):
    assert test_maze.is_exit((7,13)) == True

# pmazeGame.py
# Maze class that can be called to run the game.
# Author: Bryan

from controllers.maze_controller import MazeController
from models.maze import Maze
from views.maze_view import MazeView
import os

class MazeGame:
    """
    This class creates and calls the controller to run the game.
    """
    def __init__(self):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        self._maze_path = os.path.join(os.path.dirname(curr_dir), "maze.txt") 


    def play_maze(self):
        """Runs the game"""
        maze = Maze(self._maze_path)
        #The start position of the palyer
        start_pos = maze.player.space
        view = MazeView(start_pos)
        #Run the game
        maze_controller = MazeController(maze, view)
        maze_controller.play_game()
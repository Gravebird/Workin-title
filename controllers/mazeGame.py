from controllers.maze_controller import MazeController
from models.maze import Maze
from views.maze_view import MazeView

class MazeGame:
    """
    This class creates and calls the controller to run the game.
    """
    def __init__(self):
        pass


    def play_maze(self):
        maze = Maze("maze.txt")
        start_pos = maze.player_space
        view = MazeView(start_pos)
        maze_controller = MazeController(maze, view)
        maze_controller.play_game()
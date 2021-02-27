from controllers.maze_controller import MazeController

class MazeGame:
    """
    This class creates and calls the controller to run the game.
    """
    def __init__(self):
        pass


    def run(self):
        maze_controller = MazeController()
        maze_controller.play_game()
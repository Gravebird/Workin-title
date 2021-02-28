from models.maze import Maze
from views.maze_view import MazeView
import pygame
import pygame.locals

class MazeController:
    """
    This class contains the functions that control how the other classes display
    and handle the maze.

    :param maze_: the maze model
    :type maze_: Maze Object

    :param view_: The view (GUI) of the maze
    :type view_: MazeView Object
    """
    def __init__(self, maze_, view_):
        self._maze = maze_
        self._view = view_
    

    def play_game(self):
        """
        This function will start the game loop and call for user input, and handle
        game logic.
        """
        pygame.init()
        clock = pygame.time.Clock()
        input_timer = 0
        framerate = 10

        while not self._maze.is_player_at_exit():
            clock.tick(framerate)
            self._view.display(self._maze)
            keys = pygame.key.get_pressed()
            input_direction = self.get_input(keys)

            if input_direction != None and input_timer == 0:
                input_timer = framerate
                (Px, Py) = self._maze.player_space
                (Px, Py) = self.move_player(input_direction, Px, Py)

                if self._maze.is_item((Px, Py)):
                    self._maze.player.backpack = self._maze.map[Px][Py]

                self._maze.player_space = (Px, Py)

            ##################################
                print(f"Backpack contains: {self._maze.player.backpack}")
            
            if input_timer > 0:
                input_timer -= 1
        
        ### Player has reached the end of the maze ###

        if (len(self._maze.player.backpack) < 4):
            # Player loses (did not collect all 4 items!)
            print("You Lose!")
        else:
            # Player wins!
            print("You Win!")


    def get_input(self, keys):
        """
        Function to check whether a keyboard button was pressed, and return a
        string reprentation of that button. In this case we are converting to
        wasd format (Up = w, Left = a, Down = s, Right = d).

        :return: The direction the user inputted
        :rtype: str (len 1)
        """
        dir = None
        if keys[pygame.locals.K_RIGHT]:
            dir = "d"
        elif keys[pygame.locals.K_LEFT]:
            dir = "a"
        elif keys[pygame.locals.K_UP]:
            dir = "w"
        elif keys[pygame.locals.K_DOWN]:
            dir = "s"
        return dir


    def move_player(self, input_direction: str, Px: int, Py: int)-> tuple:
        """Move the player by user's input (ASWD)

        :param direction: 4 directions (ASWD) that the player moves
        :type direction: str
        :param Px: row of the Player's current location
        :type Px: int
        :param Py: column of the Player's current location
        :type Py: int
        :return: row and column (x,y coordiantes) of the Player's most updated location
        :rtype: turple
        """
        # Move up (w)
        if input_direction == "w":
            if self._maze.can_move_to(Px - 1, Py) == True:
                Px -= 1
                print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
        # Move down (s)
        if input_direction == "s":
            if self._maze.can_move_to(Px + 1, Py) == True:
                Px += 1
                print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
        # Move left (a)
        if input_direction == "a":
            if self._maze.can_move_to(Px, Py -1) == True:
                Py -= 1
                print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
        # Move right (d)
        if input_direction == "d":
            if self._maze.can_move_to(Px, Py + 1) == True:
                Py += 1
                print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
    
        return (Px, Py)
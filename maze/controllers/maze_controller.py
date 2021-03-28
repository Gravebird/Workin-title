# maze_controller.py
# Primary controller for the maze.
# Author: Xavier, Leo, Jennie, Bryan, Tiras

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
        """Initializes the instance"""
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
            #clock.tick(framerate)
            self._view.display(self._maze)
            waiting_for_input = True
            previous_input = None #Default values
            input_direction = None #Default values

            while waiting_for_input:
                clock.tick(framerate)
                #Get user input
                keys = pygame.key.get_pressed()
                input_direction = self.get_input(keys)
                #If the input is none, check to see if the previous input wasn't
                #If there's a current input, begin the countdown to move.

                if input_timer <= 0 or input_direction == None:
                    #Check if current input is same as previous input, but not None
                    if input_direction != None and previous_input == input_direction:
                        waiting_for_input = False
                        #Counts down each frame (1s) to move
                        input_timer -= 1
                        if input_timer <= 0:
                            #Update player position
                            input_timer = framerate
                            (Px, Py) = self._maze.player.space
                            self.move_player(input_direction, Px, Py)

                    #Check if previously had an input, but user let go
                    elif previous_input != None and input_direction == None:
                        waiting_for_input = False
                        input_timer = 0
                        #Update player position
                        (Px, Py) = self._maze.player.space
                        self.move_player(previous_input, Px, Py)
                        previous_input = None

                    #Check if user pressed a key
                    elif input_direction != None:
                        previous_input = input_direction
                        input_timer = framerate
                        
                else:
                    input_timer -= 1
                
                pygame.event.pump()

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
        if keys[pygame.locals.K_RIGHT] or keys[pygame.locals.K_d]:
        #Accepts Right Key or D to move Right
            dir = "d"
        elif keys[pygame.locals.K_LEFT] or keys[pygame.locals.K_a]:
        #Accepts Left Key or A to move Left
            dir = "a"
        elif keys[pygame.locals.K_UP] or keys[pygame.locals.K_w]:
        #Accepts Up Key or W to move Up
            dir = "w"
        elif keys[pygame.locals.K_DOWN] or keys[pygame.locals.K_s]:
        #Accepts Down Key or D to move Down
            dir = "s"
        return dir


    def move_player(self, input_direction: str, Px: int, Py: int)-> None:
        """Move the player by user's input (WASD)

        :param direction: 4 directions (WASD) that the player moves
        :type direction: str

        :param Px: row of the Player's current location
        :type Px: int

        :param Py: column of the Player's current location
        :type Py: int
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

        if self._maze.is_item((Px, Py)):
            self._maze.player.backpack = self._maze.map[Px][Py]
            self._maze.remove_item_from_maze((Px, Py))
        self._maze.player.space = (Px, Py)
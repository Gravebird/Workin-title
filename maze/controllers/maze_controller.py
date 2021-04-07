# maze_controller.py
# Primary controller for the maze.
# Author: Xavier, Leo, Jennie, Bryan, Tiras

from models.maze import Maze
from views.maze_view import MazeView
from models.score import Score
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
        framerate = 10
        self._view.display(self._maze)
        key_held_down = 0
        prev_input = None

        # Maximum allowed time for the game is 100s
        max_time = 100
        time_left = max_time

        while not self._maze.is_player_at_exit() and time_left > 0:
            # Game loop, while the player has not reached the exit
            time_elapsed = clock.tick(framerate)
            keys = pygame.key.get_pressed()
            self._view.time_remaining(time_left)
            input_direction = self.get_input(keys)


            if input_direction != None:
                if prev_input == input_direction and key_held_down < framerate:
                    key_held_down += 1
                else:
                    (Px, Py) = self._maze.player.space
                    self._view.player_update(Py, Px, " ")
                    self.move_player(input_direction, Px, Py)
                    (Px, Py) = self._maze.player.space
                    self._view.player_update(Py, Px, "P")
                    key_held_down = 0
            
            prev_input = input_direction

            pygame.event.pump()
            
            time_left = time_left - time_elapsed / 1000
            # print(f"{time_left:.2f}")

        ### Player has reached the end of the maze or time is up ###

        if (len(self._maze.player.backpack) < 4 or time_left <= 0):
            # Player loses (did not collect all 4 items or time is up!)
            print("You Lose!")
            explosion_count = 0
            (Px, Py) = self._maze.player.space
            while explosion_count < 25:
                clock.tick(framerate)
                self._view.explosion_animation(Px, Py, explosion_count, self._maze)
                explosion_count += 1
            time_out = 0
            
            #pygame.time.delay(5 * 1000)
            while time_out < (5 * framerate): #To display for 5 seconds
                clock.tick(framerate)
                print("DISPLAYING LOSS")
                self._view.end_screen('loss')
                time_out += 1
        else:
            # Player wins!
            self._view.end_screen('win')

            print("You Win!")
            points = round((time_left * 100))
            print(f"Your score: {points}")

            name = input("Input your username for the Scoreboard: ")

            user_score = Score(name, points)
            user_score.send_score()

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
                # print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
        # Move down (s)
        if input_direction == "s":
            if self._maze.can_move_to(Px + 1, Py) == True:
                Px += 1
                # print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
        # Move left (a)
        if input_direction == "a":
            if self._maze.can_move_to(Px, Py -1) == True:
                Py -= 1
                # print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
        # Move right (d)
        if input_direction == "d":
            if self._maze.can_move_to(Px, Py + 1) == True:
                Py += 1
                # print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate

        if self._maze.is_item((Px, Py)):
            self._maze.player.backpack = self._maze.map[Px][Py]
            self._maze.remove_item_from_maze((Px, Py))
            self._view.backpack_contents(self._maze.player.backpack)

        self._maze.player.space = (Px, Py)
# maze_view.py
# Viewport controller for the maze.
# Author: Xavier, Bryan

from models.maze import Maze
import pygame
from os import path

class MazeView:
    """
    This class is used to display the contents of the maze model in a GUI.

    :param _width: The width of the GUI
    :type _width: int

    :param _height: The height of the GUI
    :type _height: int

    :param start_pos: The space where the player starts
    :type start_pos: A tuple | X Y coordinates
    """
    CURR_DIR = path.dirname(path.abspath(__file__))
    IMG_DIR = path.join(path.dirname(CURR_DIR), "images")
    def __init__(self, start_pos: tuple):
        self._width = 720
        self._height = 480
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._entry = start_pos

        self._explosion = [pygame.image.load(self.find_img(f"explosion/frame_{i}.png")) for i in range(25)]

        pygame.display.flip()

    @classmethod
    def find_img(cls, image):
        """
        Finds an image relative to the image directory

        :param image: Image to be found
        :type image: str
        :return: Path to image
        :rtype: str
        """
        return path.join(cls.IMG_DIR, image)

    def backpack_contents(self,item_list):
        """prints the back pack and its contents

        :param item_list: list of items in backpack
        :type item_list: list
        """
        pix = 40
        y = 11
        screen_s = self._screen
        bag = pygame.image.load(self.find_img('bag.png'))
        screen_s.blit(pygame.transform.smoothscale(bag, (pix,pix)), ((10 *pix), ( y * pix)))
        count = 10
        for type_e in item_list:
            count += 1
            x = count
            if type_e == "A":
                #Load Item1
                item1 = pygame.image.load(self.find_img('blue.png'))
                screen_s.blit(pygame.transform.smoothscale(item1, (pix,pix)), ((x *pix), (y * pix)))
            elif type_e == "B":
                #Load Item2
                item2 = pygame.image.load(self.find_img('blue2.png'))
                screen_s.blit(pygame.transform.smoothscale(item2, (pix,pix)), ((x *pix), (y * pix)))
            elif type_e == "C":
                #Load Item3
                item3 = pygame.image.load(self.find_img('fat head.png'))
                screen_s.blit(pygame.transform.smoothscale(item3, (pix,pix)), ((x * pix), (y * pix)))
            elif type_e == "D":
                #Load Item4
                item4 = pygame.image.load(self.find_img('pink head.png'))
                screen_s.blit(pygame.transform.smoothscale(item4, (pix,pix)), ((x *pix), (y * pix)))


    def time_remaining(self, time):
        """prints out current time

        :param time: the time left in the game
        :type time: int
        """
        font = pygame.font.SysFont('Consolas', 20)
        pygame.draw.rect(self._screen, (0,0,0), [0, 440, 220, 40])
        self._screen.blit(font.render(f'Time remaining: {time:0.0f}', True, (255,255,255)), (0, 440))



    def display(self, maze):
        """
        Draws the contents of the maze model to a GUI.
        """
        self._screen = pygame.display.set_mode((self._width, self._height))

        level = 0

        for row in maze.map:
            spot = 0
            for pos in row:
                self.tile_print(spot, level, pos, self._screen)
                spot += 1
            level += 1
        
        self.tile_print_player(maze.player.space[1], maze.player.space[0], self._screen)
        print(maze.player.space)

        pygame.display.flip()

    def player_update(self, x, y, type_e):
        """
        class to solely draw player and redraw their last spot.

        :param x: x coordinate
        :type x: int
        :param y: y coordinate
        :type y: int
        :param type_e: type player, or old spot
        :type type_e: str
        """
        self.tile_print(x, y, type_e, self._screen)
        pygame.display.flip()


    def tile_print_player(self, x, y, screen_s):
        """
        This method blits the player (cathorse) onto the screen. This method should
        be called after all other blitting has been completed, so the cathorse
        appears on top of the other images.
        """
        pix = 40
        #Load the player
        pllayer = pygame.image.load(self.find_img("cathorse.png")) #Cathorse.
        screen_s.blit(pygame.transform.smoothscale(pllayer, (pix,pix)), ((x *pix), (y * pix)))


    def tile_print(self, x, y, type_e, screen_s):
        """
        this method blits and loads all the images. 
        will be made a class at a later date
        
        :param x: x coordinate of tile
        :type x: int
        
        :param y: y coordinate of tile
        :type y: int 
        
        :param type_e: the kind of type to be displayed
        :type type_e: str
        
        :param screen_s: the screen surface to be drawn to
        :type screen_s: pygame display surface
        
        pix can be used to adjust the size of each tile.
        """
        pix = 40

        if type_e == 'X':
            #Loads the walls
            tree = pygame.image.load(self.find_img('trees.png'))
            screen_s.blit(pygame.transform.smoothscale(tree, (pix,pix)), (x *pix, y * pix))
        elif type_e ==' ' or type_e == "P":
            #Loads walkable tiles
            walktile = pygame.image.load(self.find_img('walkintile.png'))
            screen_s.blit(pygame.transform.smoothscale(walktile, (pix,pix)), (x *pix, y * pix))
        elif type_e == 'E':
            #Loads the exit
            exit_maze = pygame.image.load(self.find_img('boxcat.png'))
            screen_s.blit(pygame.transform.smoothscale(exit_maze, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "A":
            #Load Item1
            item1 = pygame.image.load(self.find_img('birds1.png'))
            screen_s.blit(pygame.transform.smoothscale(item1, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "B":
            #Load Item2
            item2 = pygame.image.load(self.find_img('birds2.png'))
            screen_s.blit(pygame.transform.smoothscale(item2, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "C":
            #Load Item3
            item3 = pygame.image.load(self.find_img('fatbird3.png'))
            screen_s.blit(pygame.transform.smoothscale(item3, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "D":
            #Load Item4
            item4 = pygame.image.load(self.find_img('pinkbird.png'))
            screen_s.blit(pygame.transform.smoothscale(item4, (pix,pix)), ((x *pix), (y * pix)))
        if type_e == "P":
            pllayer = pygame.image.load(self.find_img('cathorse.png')) #Cathorse.
            screen_s.blit(pygame.transform.smoothscale(pllayer, (pix,pix)), ((x *pix), (y * pix)))

        if self._entry[0] == y and self._entry[1] == x:
            #Load the entrance
            entry = pygame.image.load(self.find_img('holein.png'))
            screen_s.blit(pygame.transform.smoothscale(entry, (pix,pix)), ((x *pix), (y * pix)))


    def display_partial(self, maze, x, y):
        """
        This function updates the display of only a part of the maze. This is
        used when animating the explosion.

        :param maze: The maze that the player navigates
        :type maze: Maze object

        :param x: The X index of the player in the maze array
        :type x: int

        :param y: The Y index of the player in the maze array
        :type y: int
        """
        level = 0

        for row in maze.map:
            spot = 0
            for pos in row:
                if (x >= (level - 3) and x <= (level + 3)) and y >= (spot - 3) and y <= (spot + 3):
                    self.tile_print(spot, level, pos, self._screen)
                spot += 1
            level += 1
    

    def explosion_animation(self, x, y, explosion_count, maze):
        """
        Animates an explosion on the position of the player.

        :param x: The X index of the player in the maze array
        :type x: int

        :param y: The Y index of the player in the maze array
        :type y: int

        :param explosion_count: Counts what frame of the explosion we are displaying
        :type explosion_count: int

        :param maze: The maze that the player navigates
        :type maze: Maze object
        """
        pix = 40
        explosion_adj_x = 80
        explosion_adj_y = 50

        self.display_partial(maze, x, y)
        self._screen.blit(self._explosion[explosion_count], ((y * pix) - explosion_adj_y, (x * pix) - explosion_adj_x))
        pygame.display.flip()
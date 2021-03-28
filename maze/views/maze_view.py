# maze_view.py
# Viewport controller for the maze.
# Author: Xavier, Bryan

from models.maze import Maze
import pygame

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
    def __init__(self, start_pos: tuple):
        self._width = 720
        self._height = 440
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._entry = start_pos
        pygame.display.flip()

    
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

    
    def tile_print_player(self, x, y, screen_s):
        """
        This method blits the player (cathorse) onto the screen. This method should
        be called after all other blitting has been completed, so the cathorse
        appears on top of the other images.
        """
        pix = 40
        #Load the player
        pllayer = pygame.image.load('images/cathorse.png') #Cathorse.
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
            tree = pygame.image.load('images/trees.png')
            screen_s.blit(pygame.transform.smoothscale(tree, (pix,pix)), (x *pix, y * pix))
        elif type_e ==' ' or type_e == "P":
            #Loads walkable tiles
            walktile = pygame.image.load('images/walkintile.png')
            screen_s.blit(pygame.transform.smoothscale(walktile, (pix,pix)), (x *pix, y * pix))
        elif type_e == 'E':
            #Loads the exit
            exit_maze = pygame.image.load('images/boxcat.png')
            screen_s.blit(pygame.transform.smoothscale(exit_maze, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "A":
            #Load Item1
            item1 = pygame.image.load('images/birds1.png')
            screen_s.blit(pygame.transform.smoothscale(item1, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "B":
            #Load Item2
            item2 = pygame.image.load('images/birds2.png')
            screen_s.blit(pygame.transform.smoothscale(item2, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "C":
            #Load Item3
            item3 = pygame.image.load('images/fatbird3.png')
            screen_s.blit(pygame.transform.smoothscale(item3, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "D":
            #Load Item4
            item4 = pygame.image.load('images/pinkbird.png')
            screen_s.blit(pygame.transform.smoothscale(item4, (pix,pix)), ((x *pix), (y * pix)))

        if self._entry[0] == y and self._entry[1] == x:
            #Load the entrance
            entry = pygame.image.load('images/holein.png')
            screen_s.blit(pygame.transform.smoothscale(entry, (pix,pix)), ((x *pix), (y * pix)))
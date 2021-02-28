from models.maze import Maze
import pygame

class MazeView:
    """
    This class is used to display the contents of the maze model in a GUI.

    :param _width: The width of the GUI
    :type _width: int

    :param _height: The height of the GUI
    :type _height: int
    """
    def __init__(self):
        self._width = 1000
        self._height = 600
        self._screen = pygame.display.set_mode((self._width, self._height))
        self.tile_print(0, 0, "player", self._screen)
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
        
        pygame.display.flip()
    

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
            tree = pygame.image.load('images/trees.png')
            screen_s.blit(pygame.transform.smoothscale(tree, (pix,pix)), (x *pix, y * pix))
        elif type_e ==' ':
            walktile = pygame.image.load('images/walkintile.png')
            screen_s.blit(pygame.transform.smoothscale(walktile, (pix,pix)), (x *pix, y * pix))
        elif type_e == 'E':
            exit_maze = pygame.image.load('images/boxcat.png')
            screen_s.blit(pygame.transform.smoothscale(exit_maze, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "A":
            item1 = pygame.image.load('images/birds1.png')
            screen_s.blit(pygame.transform.smoothscale(item1, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "B":
            item2 = pygame.image.load('images/birds2.png')
            screen_s.blit(pygame.transform.smoothscale(item2, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "C":
            item3 = pygame.image.load('images/fatbird3.png')
            screen_s.blit(pygame.transform.smoothscale(item3, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "D":
            item4 = pygame.image.load('images/pinkbird.png')
            screen_s.blit(pygame.transform.smoothscale(item4, (pix,pix)), ((x *pix), (y * pix)))
        elif type_e == "P":
            pllayer = pygame.image.load('images/cathorse.png')
            screen_s.blit(pygame.transform.smoothscale(pllayer, (pix,pix)), ((x *pix), (y * pix)))
        """    

        I was having trouble with getting the hole to stay after the player moved.
        Commented it out for now, we can figure this out later... - Bryan, Feb 27

        elif type_e == "S":
            entry = pygame.image.load('images/holein.png')
            screen_s.blit(pygame.transform.smoothscale(entry, (pix,pix)), ((x *pix), (y * pix)))
        """
#The primary core of the [WORKIN' TITLE]. The core game will be run through here.
#Created through the collaboration of
#Tiras Gimpel
#Kit Ho (Leo) Li
#Bryan Rainbow
#Jennie Wu
#Xavier El Chantiry


from maze import Maze
import pygame

m1 = Maze("maze.txt")

(Px, Py) = m1.find_player_space()


def move_player(direction: str, Px: int, Py: int)-> tuple:
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
        if m1.can_move_to(Px - 1, Py) == True:
            Px -= 1
            print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
    # Move down (s)
    if input_direction == "s":
        if m1.can_move_to(Px + 1, Py) == True:
            Px += 1
            print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
    # Move left (a)
    if input_direction == "a":
        if m1.can_move_to(Px, Py -1) == True:
            Py -= 1
            print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
    # Move right (d)
    if input_direction == "d":
        if m1.can_move_to(Px, Py + 1) == True:
            Py += 1
            print(f"\nPlayer location at row {Px}, col {Py}") # new coordinate
    
    return (Px, Py)


# Initial Screen Display (Start)
(width, height) = (1000, 600)
screen = pygame.display.set_mode((width, height))
m1.display(screen) 
m1.tile_print(0, 0, "player", screen)
pygame.display.flip()


# Game Loop (May update later for the input/controller method to read from pygame keypress)
while (m1.is_exit((Px, Py)) == False) or (len(m1.player.backpack) < 4):
    input_direction = input("Please enter a direction (a/s/w/d): ")
    (Px, Py) = move_player(input_direction, Px, Py)
        
    if m1.is_item((Px, Py)) == True:
        # Put the item into the backpack and update the map
        m1.player.backpack = m1.map[Px][Py]
        m1.map[Px][Py] = " "


    # Re-draw
    (width, height) = (1000, 600)
    screen =pygame.display.set_mode((width, height))
    m1.display(screen) 
    m1.tile_print(Py, Px, "player", screen)
    pygame.display.flip()

    ##################################
    print(f"Backpack contains: {m1.player.backpack}")
    


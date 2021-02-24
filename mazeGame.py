#The primary core of the [WORKIN' TITLE]. The core game will be run through here.
#Created through the collaboration of
#Tiras Gimpel
#Kit Ho (Leo) Li
#Bryan Rainbow
#Jennie Wu
#Xavier El Chantiry


from maze import Maze

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
    if direction == "w":
        if m1.can_move_to(Px - 1, Py) == True:
            Px -= 1
            print(Px, Py) # new coordinate
    # Move down (s)
    if direction == "s":
        if m1.can_move_to(Px + 1, Py) == True:
            Px += 1
            print(Px, Py) # new coordinate
    # Move left (a)
    if direction == "a":
        if m1.can_move_to(Px, Py -1) == True:
            Py -= 1
            print(Px, Py) # new coordinate
    # Move right (d)
    if direction == "d":
        if m1.can_move_to(Px, Py + 1) == True:
            Py += 1
            print(Px, Py) # new coordinate
    
    return (Px, Py)


while (m1.is_exit((Px, Py)) == False) or (len(m1.player.backpack) < 4):
    input_direction = input("Please enter a direction (a/s/w/d): ")
    (Px, Py) = move_player(input_direction, Px, Py)
        
    if m1.is_item((Px, Py)) == True:
        # Put the itme into the backpack and update the map
        m1.player.backpack = m1.map[Px][Py]
        m1.map[Px][Py] = " "

    
    # For test only
    print(m1.player.backpack)
    m1.display() 
    # For test only

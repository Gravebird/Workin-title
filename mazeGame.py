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

while m1.is_exit((Px, Py)) == False:
    input_direction = input("Please enter a direction (a/s/w/d): ")
     # Move up (w)
    if input_direction == "w":
        if m1.can_move_to(Px - 1, Py) == True:
            Px -= 1
            print(Px, Py) # new coordinate
    # Move down (s)
    if input_direction == "s":
        if m1.can_move_to(Px + 1, Py) == True:
            Px += 1
            print(Px, Py) # new coordinate
    # Move left (a)
    if input_direction == "a":
        if m1.can_move_to(Px, Py -1) == True:
            Py -= 1
            print(Px, Py) # new coordinate
    # Move right (d)
    if input_direction == "d":
        if m1.can_move_to(Px, Py + 1) == True:
            Py += 1
            print(Px, Py) # new coordinate
    
# FIXME: Px, Py may get out of range, 
# may need to update .can_move_to() - Leo 2/4/21
   
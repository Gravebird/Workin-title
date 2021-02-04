# maze.py
# Create a class Maze to store the maze map
# Author: Leo, Bryan


import random
from player import Player


class Maze:
    """ Define the Maze structure of the project
    """
    def __init__(self, filename):
        """Initialiation

        :param filename: File of the maze map's structure
        :type filename: string

        Store the maze map into 2D List (_map)
        """
        mazeList = []
        tmpList = []
        with open (filename, 'r') as f:
            tmpList = [line.strip("\n") for line in f.readlines()]

        for item in tmpList:
            mazeList.append(list(item)) 

        self._map = mazeList
        self._player = Player()
        self._player_space = self.find_player_space()
        self._empty_spaces = self.find_empty_spaces()
        self.add_object_to_maze("A")
        self.add_object_to_maze("B")
        self.add_object_to_maze("C")
        self.add_object_to_maze("D")


    def find_player_space(self):
        """
        Searches the maze for the space that the player is occupying.

        This function is called when the maze is created, and then the maze
        will track the player as they move, so there is no need to call this
        function again.

        :return: the space the player is found in
        :rtype: a tuple of two ints (x and y index of the space)

        :raises Exception: if the player cannot be found
        """
        space_of_player = None

        for x, row in enumerate(self._map):
            for y, content in enumerate(row):
                if content == 'P':
                    space_of_player = (x, y)
                    break

        if space_of_player == None:
            raise Exception("Could not find player in maze!")

        return space_of_player


    def can_move_to(self, row, col):
        """Method to check if a position is empty

        :param row: row number
        :type row: integer
        :param col: column number
        :type col: integer
        :return: True for empty; False otherwise
        :rtype: Boolean
        """
        able_to_move = True
        
        if self._map[row][col] == 'X':
            able_to_move = False

        return able_to_move


    def is_item(self, space):
        """
        Checks if the specified space contains an item. It does this by looking
        at the content of the maze array at that location. If it sees X (wall),
        P (player), or an empty space it knows that space is not an item.
        Any other value in the space counts as an item (may change this later)

        :param space: The space to check for an item
        :type space: A tuple containing two ints (x and y index of the space)
        """
        content = self._map[space[0]][space[1]]
        item_in_space = True

        if content != ' ' and content != 'P' and content != 'X' \
            and content != 'E':
            item_in_space = False

        return item_in_space


    def is_exit(self, space):
        """
        Checks if the specified space contains the exit.

        :param space: The space to check
        :type space: A tuple containing two ints (x and y index of the space)

        :return: true if the space contains the exit, false otherwise
        :rtype: bool
        """
        is_exit = False
        if self._map[space[0]][space[1]] == 'E':
            is_exit = True
        return is_exit


    def display(self):
        """Method to display the map (print)
        """
        for row in self._map:
            for pos in row:
                print(pos, end="")
            print("\n")


    def find_empty_spaces(self):
        """ 
        Creates an array containing the x and y position of each empty space in
        the maze.

        :return: The array of empty spaces
        :rtype: array of tuples (x and y values)
        """
        empty_spaces = []

        for x, row in enumerate(self._map):
            for y, content in enumerate(row):
                if self.can_move_to(x, y) \
                    and self._player_space != (x,y) \
                    and content != 'E':
                    empty_spaces.append((x, y))

        return empty_spaces


    def remove_from_empty_spaces_list(self, space):
        """
        Removes the given space from the list of empty spaces.
        This function is called every time an object is placed in the maze, so
        it should not ever attempt to delete a space that does not exist in the
        list. If this does happen it will raise a ValueError (from list.remove 
        definition)

        :param space: The space to remove
        :type space: A tuple containing two ints (x and y index of the space)
        """
        self._empty_spaces.remove(space)

    
    def place_object(self, space, letter):
        """
        This function puts an object in the space given, which must be an empty
        space.

        For now the object is represented by a letter, but in the future it will
        likely need to be an actual object in the programming sense of the word.

        :param space: The location of the space where the item is to be placed
        :type space: a tuple containing two ints (x and y index of the space)

        :param letter: The letter to be used to represent the object
        :type letter: str (but only 1 letter)

        :raises ValueError: If more/less than 1 letter is passed in

        :raises Exception: If the given space is not empty
        """
        if len(letter) != 1:
            raise ValueError("Can only add 1 letter to the maze as an object!")
        if self.can_move_to(space[0], space[1]) == False:
            raise Exception("Cannot add an object to a non-empty space!")

        self._map[space[0]][space[1]] = letter
        self.remove_from_empty_spaces_list(space)


    def add_object_to_maze(self, letter):
        """
        Adds the specified letter (representing an object in the maze) to the
        maze.
        """
        space = self.find_random_spot()
        self.place_object(space, letter)


    def find_random_spot(self):
        """
        Finds a random empty space in the maze. 

        :return: a tuple containing the x and y index values of the randomly
        selected empty space
        :rtype: a tuple containing two integers
        """
        random_index = random.randint(0, len(self._empty_spaces) - 1)
        return self._empty_spaces[random_index]


    def print_maze_content(self, space):
        """
        This function is for testing purposes.

        It will print the value stored inside the maze at the designated space.

        :param space: A tuple containing two integers - the x and y indexes of
        the space to print
        """
        content = self._map[space[0]][space[1]]
        if content == " ":
            content = "Empty"
        print("Content of space: {}".format(content))


################################
if __name__ == "__main__":
    m1 = Maze("maze.txt")
    # result = m1.check(0,3)
    # print(result)
    m1.display()

    random_space = m1.find_random_spot()
    print("Random space indexes: x={}, y={}".format(random_space[0],\
        random_space[1]))
    m1.print_maze_content(random_space)

    print("\nTesting: Fill maze with items until no room left...\n")

    while len(m1._empty_spaces) >= 1:
        m1.add_object_to_maze("I")
    
    m1.display()
    
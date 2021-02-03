# maze.py
# Create a class Maze to store the maze map
# Author: Leo


import random


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
        self.empty_spaces = self.find_empty_spaces()


    def check(self, row, col):
        """Method to check if a position is empty

        :param row: row number
        :type row: integer
        :param col: column number
        :type col: integer
        :return: True for empty; False otherwise
        :rtype: Boolean
        """
        if self._map[row][col] == ' ':
            return True
        else:
            return False


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
                if self.check(x, y):
                    empty_spaces.append((x, y))

        return empty_spaces


    def find_random_spot(self):
        """
        Finds a random empty space in the maze. 

        :return: a tuple containing the x and y index values of the randomly
        selected empty space
        :rtype: a tuple containing two integers
        """
        random_index = random.randint(0, len(self.empty_spaces) - 1)
        return self.empty_spaces[random_index]


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
    
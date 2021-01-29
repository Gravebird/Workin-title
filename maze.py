# maze.py
# Create a class Maze to store the maze map
# Author: Leo


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


    def find_random_spot(self):
        # to be code
        # FIXME
        print(len(self._map))       # number of rows
        print(len(self._map[0]))    # number of columns
        pass



################################
if __name__ == "__main__":
    m1 = Maze("maze.txt")
    # result = m1.check(0,3)
    # print(result)
    m1.display()
    m1.find_random_spot()
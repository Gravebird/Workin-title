# player.py
# A player in a maze
# Author: Bryan


class Player:
    """
    This class represents a player in a maze, with a backpack to hold any
    items they find along the way.

    :param space_: The space of the player
    :type space: A tuple of ints | X Y coordinates
    """
    def __init__(self, space_):
        """
        Initializes a player.
        """
        self._backpack = []
        self._space = space_
    

    @property
    def backpack(self):
        return self._backpack
    
    @backpack.setter
    def backpack(self, item):
        self._backpack.append(item)

    @property
    def space(self):
        return self._space

    @space.setter
    def space(self, new_space: tuple):
        """
        Updates the space variable with the new player space
        """
        self._space = new_space
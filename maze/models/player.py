# player.py
# A player in a maze
# Author: Bryan


class Player:
    """
    This class represents a player in a maze, with a backpack to hold any
    items they find along the way.
    """
    def __init__(self):
        """
        Initializes a player.
        """
        self._backpack = []
    

    @property
    def backpack(self):
        return self._backpack
    
    @backpack.setter
    def backpack(self, item):
        self._backpack.append(item)
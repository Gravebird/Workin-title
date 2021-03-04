#The primary core of the [WORKIN' TITLE]. The core game will be run through here.
#Created through the collaboration of
#Tiras Gimpel
#Kit Ho (Leo) Li
#Bryan Rainbow
#Jennie Wu
#Xavier El Chantiry

from controllers.mazeGame import MazeGame

if __name__ == "__main__":
    #This creates the game instance and runs it.
    maze_game = MazeGame()
    maze_game.play_maze()
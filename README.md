# Workin-title
A maze game called [WORKIN' TITLE]. Made for ACIT-2515 as a final project.


# Project Structure
Models:
    maze: read and store the maze map
    player: contains the backpack which stores the items collected
Views:
    maze_view: display the maze map and tiles (player, items, exit)
Controllers:
    maze_controller: main controller contains logic of the game
    mazeGame: setup required objects and calls controller to run the game


# Dependencies
pygame==2.0.0


# How to run
python main.py


# How to control
User can control the momvent of the player by using either arrow keys or ASWD keys. The goal is to collect all 4 items in the maze.


# AOB (Any Other Business)
User is not able to go outside of the grid.
User is required to collect all 4 items and then arrives the exit.

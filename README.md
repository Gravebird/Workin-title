![Horse Cat Image](maze/images/cathorse.png)
# Workin-title
A maze game called [WORKIN' TITLE]. Made for ACIT-2515 as a final project.


# Project Structure
Models:
    
    maze: read and store the maze map
    
    player: contains the backpack which stores the items collected
    
    score: Manages and saves information on a user's score
       
Views:

    maze_view: display the maze map and tiles (player, items, exit)
    
Controllers:

    maze_controller: main controller contains logic of the game
    
    mazeGame: setup required objects and calls controller to run the game
    
    score_controller: Controls the json file for the webserver. Manages user's highscores

# Dependencies
* astroid==2.4.2
* certifi==2020.12.5
* chardet==4.0.0
* click==7.1.2
* colorama==0.4.4
* Flask==1.1.2
* idna==2.10
* isort==5.7.0
* itsdangerous==1.1.0
* Jinja2==2.11.3
* lazy-object-proxy==1.4.3
* MarkupSafe==1.1.1
* mccabe==0.6.1
* pygame==2.0.0
* pylint==2.6.0
* requests==2.25.1
* six==1.15.0
* toml==0.10.2
* urllib3==1.26.4
* Werkzeug==1.0.1
* wrapt==1.12.1

These can also be installed using the requirements.txt file provided.
To do so, use `pip install -r requirements.txt` in the game directory.

# How to run
The maze game can be easily run by running the main.py program.
In the maze directory, use:
`python main.py`

# How to run Web API
The web server used to store highscores is accessible through the Web filepath.
In this filepath, simple run:
`python server.py`

This will begin hosting the server on your local machine at port 5000.
If you have the server running right now, you can access it ![here!](http://127.0.0.1:5000/)
Going to that web server's page will instantly display any scores it has stored. To store new scores, just win the game!

# How to control
User can control the momvent of the player by using either arrow keys or WASD keys. 
By holding down a key, the player will move once every second.
By tapping a key, the player will move each press.

The goal is to collect all 4 items in the maze and then reach the exit before the time runs out.
Time limit is 100 seconds.

# AOB (Any Other Business)
User is not able to go outside of the grid.
User is required to collect all 4 items and then arrives the exit.

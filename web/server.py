import sys
import os
from flask import Flask, render_template, request
from score_controller import ScoreController
import json

curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(curr_dir))
#This MESS of sys path is just to make it possible to import the score model
#   from the maze game path.
from maze.models.score import Score

#To ensure we can always find the .json
JSON_FILEPATH = os.path.join(curr_dir, "scores.json") 

app = Flask(__name__)
data = ScoreController(JSON_FILEPATH)


@app.route("/")
def show_scores():
    """
    Displayes all current scores, ranked by highest score
    """
    return render_template('scores.html', scores=sorted(data._scores, reverse=True))

@app.route("/", methods=["PUT"])
def add_score():
    """
    Adds a score to the stored scores.
    """
    try:
        json_data = request.get_json()
        new_data = json.loads(json_data)
        new_score = Score(new_data["name"], new_data["score"], new_data["date"])
        data.add_score(new_score)
        return "", 204 #Returns sucess
    except:
       return "Invalid data proivded", 400 #Returns error

if __name__ == "__main__":
    app.run()
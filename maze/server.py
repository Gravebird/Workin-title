from flask import Flask, render_template, request
from models.score import Score
from controllers.score_controller import ScoreController
import json

JSON_FILEPATH="maze/scores.json"

app = Flask(__name__)
data = ScoreController(JSON_FILEPATH)


@app.route("/")
def show_scores():
    return render_template('scores.html', scores=sorted(data._scores, reverse=True))

@app.route("/", methods=["PUT"])
def add_score():
    try:
        new_data = request.get_json()
        new_score = Score(new_data["name"], new_data["score"], new_data["date"])
        data.add_score(new_score)
        return "", 204 #Returns sucess
    except:
       return "Invalid data proivded", 400 #Returns error

if __name__ == "__main__":
    app.run()
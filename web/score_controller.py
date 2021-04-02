import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#This MESS of sys path is just to make it possible to import the score model
#   from the maze game path.
from maze.models.score import Score #It thinks there's an error when there is not.
import json

class ScoreController():
    def __init__(self, json_path):
        self._scores = []
        self._filepath = json_path
        self.load_from_json_file()

    def print_scores(self):
        for i in self._scores:
            print(f"Score: {i.name} ({i.score})")

    def add_score(self, score):
        self._scores.append(score)
        self.load_to_json_file()

    def load_to_json_file(self):
        """
        Loads json data to a .json file.
        """
        tmp_scores = []
        for i in self._scores:
            tmp_scores.append(i.to_dict())
        with open(self._filepath, 'w') as json_file:
            json.dump(tmp_scores, json_file, indent=4)

    def load_from_json_file(self):
        """
        Loads json data from a .json file.
        """
        with open(self._filepath, 'r') as json_file:
            json_data = json.load(json_file)
        for json_score in json_data:
            score = Score(
                json_score["name"],
                json_score["score"],
                json_score["date"]
                )
            self._scores.append(score)
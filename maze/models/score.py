# maze.py
# Create a class Score to store player's score
# Author: Leo


from datetime import datetime
from requests import put
import json

class Score:
    """Class Score to save player's score
        
    :param player_name_: Player's name
    :type player_name_: str
    :param score_: Player's score (last game)
    :type score_: int
    """
    TIME_FORMAT = "%Y/%m/%d"
    URL = 'http://127.0.0.1:5000/'#default self-hosted server.

    def __init__(self, player_name_, score_, time_=None):
        """self._date: get the current date & time
        """
        self._player_name = player_name_
        self._score = score_
        if time_ == None: #By default, set time to now
            self._date = datetime.now().strftime(self.TIME_FORMAT)
        elif self.verify_datetime(time_): #Otherwise, set time to the given time value
            self._date = time_

    def __str__(self):
        return f"Score: {self._score}, {self._score}"
    
    def __gt__(self, other): #For ordering by score.
        return self._score > other._score

    @property
    def name(self):
        return self._player_name


    @property
    def score(self):
        return self._score


    @property
    def date(self):
        return self._date

    @classmethod
    def verify_datetime(cls, time):
        try:
            datetime.strptime(time, cls.TIME_FORMAT)
            return True
        except:
            raise ValueError("Incorrect datetime format")
            
    @staticmethod
    def from_json(json_str):
        """Convert JSON string into Score object

        :param json_str: JSON string
        :type json_str: str
        :return: Score object
        :rtype: Score
        """
        new_score = Score.from_dict(json.loads(json_str))
        return new_score

    @staticmethod
    def from_dict(score_dict):
        """Convert dictionary into Score object

        :param score_dict: dictionary representation of Score
        :type score_dict: dict
        :return: Score object
        :rtype: Score
        """
        NewScore = Score(score_dict["name"], score_dict["score"], score_dict["date"])

        return NewScore

    def send_score(self):
        """
        Sends the score to the web server
        """
        r = put(self.URL, json=self.to_json()) #Put the score to the webserver
        if r.status_code == 204:
            print("\nScore submitted successfully!\n")
        else:
            print("\nAn error occurred.\nCheck to see if the web-server is running.")
            print(f"\nERROR CODE: {r.status_code}")


    def to_dict(self):
        """Convert Score object into dict

        :return: A dictionarly contains Score's attributes
        :rtype: dict
        """
        PlayerScore_dict = {
            "name": self._player_name,
            "score": self._score,
            "date": self._date
        }
        
        return PlayerScore_dict

    def to_json(self):
        """Convert dict into JSON

        :return: JSON String
        :rtype: str
        """
        return json.dumps(self.to_dict())


##################################################
if __name__ == "__main__":
    S1 = Score("Name1", 100)
    
    # print(S1.player_name)
    # print(S1.score)
    # print(S1.date)

    ### Test to_dict, to_jsont ###
    # print(S1.to_dict())
    # print((S1.to_json()))


    ### Test from_dict ###
    # score = {
    #         "name": "Leo",
    #         "score": 112,
    #         "datetime": '2021/01/01 12:13:14'
    # }
    # new = Score.from_dict(score)
    
    # print(new.player_name)
    # print(new.score)
    # print(new.date)

    ### Test from_json ###
    # JSON_STR = '{"name": "Tony", "score": 1990, "datetime": "2021/03/26 00:16:45"}'
    # print(Score.from_json(JSON_STR).player_name)
    # print(Score.from_json(JSON_STR).score)
    # print(Score.from_json(JSON_STR).date)

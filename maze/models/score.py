# maze.py
# Create a class Score to store player's score
# Author: Leo


from datetime import datetime
import json

class Score:
    """Class Score to save player's score
        
    :param player_name_: Player's name
    :type player_name_: str
    :param score_: Player's score (last game)
    :type score_: int
    """
    def __init__(self, player_name_, score_):
        """self._date: get the current date & time
        """
        self._player_name = player_name_
        self._score = score_
        self._date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


    @property
    def player_name(self):
        return self._player_name


    @property
    def score(self):
        return self._score


    @property
    def date(self):
        return self._date


    def from_json(json_str):
        """Convert JSON string into Score object

        :param json_str: JSON string
        :type json_str: str
        :return: Score object
        :rtype: Score
        """
        return Score.from_dict(json.loads(json_str))


    def from_dict(score_dict):
        """Convert dictionary into Score object

        :param score_dict: dictionary representation of Score
        :type score_dict: dict
        :return: Score object
        :rtype: Score
        """
        NewScore = Score(score_dict["name"], score_dict["score"])
        NewScore._date = score_dict["datetime"]

        return NewScore


    def to_dict(self):
        """Convert Score object into dict

        :return: A dictionarly contains Score's attributes
        :rtype: dict
        """
        PlayerScore_dict = {
            "name": self.player_name,
            "score": self.score,
            "datetime": self.date
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

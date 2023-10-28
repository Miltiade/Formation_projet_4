import json

class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
    
    def serialize(self):
        """Converts the Player object to a JSON string."""
        return json.dumps(self.__dict__)

    def deserialize(cls, json_string):
        """Converts a JSON string back into a Player object."""
        attributes = json.loads(json_string)
        return cls(**attributes)

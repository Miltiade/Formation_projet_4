import json
from model_player import Player

class Players:
    def __init__(self):
        self.players = []
    
    def add(self,player: Player)->None:
        self.players.append(player)

    def sort(self):self

    def serialize(self):
        """Converts the Player object to a JSON string."""
        return json.dumps(self.__dict__)

    def deserialize(cls, json_string):
        """Converts a JSON string back into a Player object."""
        attributes = json.loads(json_string)
        return cls(**attributes)
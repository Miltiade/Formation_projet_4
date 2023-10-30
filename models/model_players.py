import json
from model_player import Player

class Players:
    def __init__(self):
        self.players = []
    
    def add(self,player: Player)->None:
        self.players.append(player)

    def sort(self):self

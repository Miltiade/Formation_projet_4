import json

class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description, players, number_of_rounds=4, current_round=0):

        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.players = players
        self.time_control = time_control
        self.current_round = current_round
        self.rounds = []
        self.matches_played = []

    def add_player(self, player):
        self.players.append(player)
        
    def add_round(self, round):
        self.rounds.append(round)

    def serialize(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'number_of_rounds': self.number_of_rounds,
            'description': self.description,
            'players': [player.serialize() for player in self.players],
            'time_control': self.time_control,
            'current_round': self.current_round,
            'rounds': [round_.serialize() for round_ in self.rounds],
            'matches_played': [(player1.serialize(), player2.serialize()) for player1, player2 in self.matches_played]
        }


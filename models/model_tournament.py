# In models/model_tournament.py

from models.model_round import Round
from models.model_player import Player
from models.model_match import Match

class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description, player_elos, number_of_rounds=4, current_round=0, rounds=None, players=None):
        """
        Initialize a Tournament instance.

        Args:
            name (str): Name of the tournament.
            place (str): Location of the tournament.
            start_date (str): Start date of the tournament.
            end_date (str): End date of the tournament.
            time_control (str): Time control for the tournament.
            description (str): General remarks about the tournament.
            player_elos (list): List of player ELOs.
            number_of_rounds (int): Number of rounds in the tournament (default: 4).
            current_round (int): Current round number (default: 0).
            rounds (list): List of rounds (default: None).
            players (list): List of players (default: None).
        """
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.player_elos = player_elos
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        # self.matches_played = matches_played  # Commented out: it is not required by the specifications
        self.rounds = rounds if rounds is not None else []
        self.players = players if players is not None else []

    def add_player(self, player):
        # Add player to the players list
        self.players.append(player)
        # Add player's elo (as string) to the player_elos list whenever a player is added
        self.player_elos.append(str(player.elo))
        print(self.player_elos)

    @classmethod
    def message(self):
        print("toto")

    def add_round(self, round):
        # Add round to the rounds list
        self.rounds.append(round)

    def serialize(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_rounds': self.number_of_rounds,
            'description': self.description,
            'player_elos': self.player_elos,
            'time_control': self.time_control,
            'current_round': self.current_round,
            'rounds': [round_.serialize() for round_ in self.rounds],
            'players': [player.serialize() for player in self.players]
        }

    @classmethod
    def deserialize(cls, tournament_data, players):
        rounds = [Round.deserialize(round_data, players) for round_data in tournament_data.get('rounds', [])]
        players = [Player.deserialize(player_data) for player_data in tournament_data.get('players', [])]
        return cls(
            name=tournament_data['name'],
            place=tournament_data['place'],
            start_date=tournament_data['start_date'],
            end_date=tournament_data['end_date'],
            time_control=tournament_data['time_control'],
            description=tournament_data['description'],
            player_elos=tournament_data['player_elos'],
            number_of_rounds=tournament_data['number_of_rounds'],
            current_round=tournament_data['current_round'],
            rounds=rounds,
            players=players
        )
    
    '''A function that prints player_elos as a string'''
    def get_player_elos(self):
        return f"{self.player_elos}"

    '''A function that prints a tournament object as a string'''
    def __str__(self):
        return f"{self.name} - {self.start_date} to {self.end_date}"
import json
import re  # for method def_validate_elo()
# from models.model_match import Match

class Player:
    def __init__(self, first_name, family_name, date_of_birth, elo, initial_ranking, match_score, total_score, matches_played=None):
        self.first_name = first_name
        self.family_name = family_name
        self.date_of_birth = date_of_birth
        self.elo = elo  # Unique identifier for the player
        self.initial_ranking = initial_ranking
        self.match_score = match_score  # player's score in the current match
        self.total_score = total_score  # player's total score at a given time
        self.matches_played = matches_played if matches_played is not None else []

    def __str__(self):
        return f"{self.first_name} | {self.family_name} | {self.date_of_birth} | {self.elo} | {self.initial_ranking} | {self.match_score} | {self.total_score}"

    def __repr__(self):
        return f"Player('{self.first_name}', '{self.family_name}', '{self.date_of_birth}', {self.elo}, {self.initial_ranking}, {self.match_score}, {self.total_score})"

    def validate_elo(self):
        # Validate the format of the elo
        if not re.match(r'^[A-Z]{2}\d{5}$', self.elo):
            raise ValueError("ELO must be in the format of two letters followed by five digits (e.g., AB12345)")

    def serialize(self):
        # Serialize the player object to a dictionary
        return {
            'first_name': self.first_name,
            'family_name': self.family_name,
            'date_of_birth': self.date_of_birth,
            'elo': self.elo,
            'initial_ranking': self.initial_ranking,
            'match_score': self.match_score,
            'total_score': self.total_score,
            'matches_played': [match.serialize() for match in self.matches_played]  # Serialize matches played
        }

    @classmethod
    def from_dict(cls, player_data):
        # Creates a player object from a dictionary.
        return cls(
            player_data['first_name'],
            player_data['family_name'],
            player_data['date_of_birth'],
            player_data['elo'],
            player_data['initial_ranking'],
            player_data['match_score'],
            player_data['total_score']
        )

    @classmethod
    def deserialize(cls, player_data):
        # Deserialize the player object from a dictionary
        return cls(
            first_name=player_data['first_name'],
            family_name=player_data['family_name'],
            date_of_birth=player_data['date_of_birth'],
            elo=player_data['elo'],
            initial_ranking=player_data['initial_ranking'],
            match_score=player_data['match_score'],
            total_score=player_data['total_score'],
            # matches_played=[Match.deserialize(match_data) for match_data in player_data.get('matches_played', [])]

        )

    def save_to_database(self, file_path):
        # A method that converts player info into a dictionary, using "serialize" method
        # Argument is: filepath of the JSON file in which to save the players
        player_data = self.serialize()
        try:
            # Open JSON file as write
            with open(file_path, 'w') as file:
                # Use json library to format dictionary into JSON
                json.dump(player_data, file)
        except IOError:
            # Raise errors if they happen
            print("Error while saving player in database.")

    def load_from_database(self, file_path):
        # Argument is: filepath of the JSON file containing player info
        try:
            # Open JSON file as read-only
            with open(file_path, 'r') as file:
                # Use json library to load file data
                player_data = json.load(file)
            # Get player info from dictionary
            self.first_name = player_data['first_name']
            self.family_name = player_data['family_name']
            self.date_of_birth = player_data['date_of_birth']
            self.elo = player_data['elo']
            self.initial_ranking = player_data['initial_ranking']
            self.match_score = player_data['match_score']
            self.total_score = player_data['total_score']
        except FileNotFoundError:
            print("The requested JSON file does not exist.")
        except json.JSONDecodeError:
            print("Error while decoding JSON: cannot read file.")

    def display_player_info(self):
        # Display player information
        print(f"Prénom : {self.first_name}")
        print(f"Nom de famille : {self.family_name}")
        print(f"Date de naissance : {self.date_of_birth}")
        print(f"Elo : {self.elo}")
        print(f"Classement initial : {self.initial_ranking}")
        print(f"Score du match en cours : {self.match_score}")
        print(f"Score total : {self.total_score}")
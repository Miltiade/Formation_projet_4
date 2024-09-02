import json

class Player:
    
    def __init__(self, family_name, first_name, date_of_birth, elo, initial_ranking=0, match_score=0, total_score=0):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.elo = elo
        self.initial_ranking = initial_ranking
        self.match_score = match_score # player's score in the current match
        self.total_score = total_score # player's total score at a given time
        
    def __str__(self):
        return f"{self.family_name} | {self.first_name} | {self.date_of_birth} | {self.elo} |{self.initial_ranking} | {self.match_score} | {self.total_score}"
    
    def __repr__(self):
        return f"Player('{self.family_name}', '{self.first_name}', '{self.date_of_birth}', {self.elo}, {self.initial_ranking}, {self.match_score}, {self.total_score})" 
    
    def serialize(self):
        return {
            'family name': self.family_name,
            'first name': self.first_name,
            'date of birth': self.date_of_birth,
            'elo': self.elo,
            'initial_ranking': self.initial_ranking,
            'match_score': self.match_score,
            'total_score': self.total_score,
        }

    @staticmethod
    def deserialize(player_data):
        return Player(
            player_data['family name'],
            player_data['first name'],
            player_data['date of birth'],
            player_data['elo'],
            player_data['initial_ranking', 0],
            player_data.get('match_score', 0),
            player_data.get('total_score', 0)
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
            self.first_name = player_data['first name']
            self.family_name = player_data['family name']
            self.date_of_birth = player_data['date of birth']
            self.elo = player_data['elo']
            self.initial_ranking = player_data['initial_ranking']
            self.match_score = player_data['match_score']
            self.total_score = player_data['total_score']
        except FileNotFoundError:
            print("The requested JSON file does not exist.")
        except json.JSONDecodeError:
            print("Error while decoding JSON: cannot read file.")

    def display_player_info(self):
        print(f"Prénom : {self.first_name}")
        print(f"Nom de famille : {self.family_name}")
        print(f"Date de naissance : {self.date_of_birth}")
        print(f"Elo : {self.elo}")
        print(f"Classement initial : {self.initial_ranking}")
        print(f"Score du match en cours : {self.match_score}")
        print(f"Score total : {self.total_score}")
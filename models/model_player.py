import json

class Player:
    def __init__(self, name, elo, initial_ranking=0, match_score=0, total_score=0):
        self.name = name
        self.elo = elo
        self.initial_ranking = initial_ranking
        self.match_score = match_score # player's score in the current match
        self.total_score = total_score # player's total score at a given time
        self.initial_ranking = initial_ranking
        
    def __str__(self):
        return f"{self.name} | {self.elo} |{self.initial_ranking} | {self.match_score} | {self.total_score}"
    
    def serialize(self):
        return {
            'name': self.name,
            'elo': self.elo,
            'initial_ranking': self.initial_ranking,
            'match_score': self.match_score,
            'total_score': self.total_score,
        }

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
            self.name = player_data['name']
            self.elo = player_data['elo']
            self.initial_ranking = player_data['initial_ranking']
            self.match_score = player_data['match_score']
            self.total_score = player_data['total_score']
        except FileNotFoundError:
            print("The requested JSON file does not exist.")
        except json.JSONDecodeError:
            print("Error while decoding JSON: cannot read file.")

    def display_player_info(self):
        print(f"Nom : {self.name}")
        print(f"Elo : {self.elo}")
        print(f"Classement initial : {self.initial_ranking}")
        print(f"Score du match en cours : {self.match_score}")
        print(f"Score total : {self.total_score}")
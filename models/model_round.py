import datetime
from models.model_match import Match

class Round:
    def __init__(self, number, start_time=None, end_time=None):
        self.matchs = []  # List to store matches in the round
        self.number = number  # Round number
        self.name = "Round " + str(number)  # Default name for the round
        self.start_time = start_time  # Start time of the round
        self.end_time = end_time  # End time of the round

    def add_match(self, match):
        # Add a match to the round
        self.matchs.append(match)

    def auto_set_start_time(self):
        # Automatically set the start time when the round is created
        self.start_time = datetime.datetime.now()  # Set the current timestamp

    def auto_set_end_time(self):
        # Automatically set the end time when the round is completed
        self.end_time = datetime.datetime.now()  # Set the current timestamp

    def serialize(self):
        # Serialize the round object to a dictionary
        return {
            'matchs': [match.serialize() for match in self.matchs],  # Serialize each match
            'number': self.number,  # Round number
            'name': self.name,  # Round name
            'start_time': self.start_time.isoformat() if self.start_time else None,  # ISO format for start time
            'end_time': self.end_time.isoformat() if self.end_time else None  # ISO format for end time
        }

    @classmethod
    def deserialize(cls, data, players):
        # Deserialize the round object from a dictionary
        round_obj = cls(
            number=data['number'],  # Round number
            start_time=datetime.datetime.fromisoformat(data['start_time']) if data['start_time'] else None,  # Parse start time
            end_time=datetime.datetime.fromisoformat(data['end_time']) if data['end_time'] else None  # Parse end time
        )
        # Set the match's attribute after the object is created
        # Deserialize each match using the provided players
        round_obj.matchs = [Match.deserialize(match_data, players) for match_data in data.get('matchs', [])]
        return round_obj
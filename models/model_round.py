import datetime
from models.model_match import Match

class Round:
    def __init__(self, number, start_time=None, end_time=None):
        self.matchs = []
        self.number = number
        self.name = "Round " + str(number)
        self.start_time = start_time
        self.end_time = end_time
        
    def add_match(self, match):
        self.matchs.append(match)

    def create(self):
        # Set the start time when the round is created
        self.start_time = datetime.datetime.now()

    def mark_as_completed(self):
        # Set the end time when the round is marked as completed
        self.end_time = datetime.datetime.now()

    def serialize(self):
        # Serialize the round object to a dictionary
        return {
            'matchs': [match.serialize() for match in self.matchs],
            'number': self.number,
            'name': self.name,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None
        }

    @classmethod
    def deserialize(cls, data):
        # Deserialize the round object from a dictionary
        round_obj = cls(
            number=data['number'],
            start_time=datetime.datetime.fromisoformat(data['start_time']) if data['start_time'] else None,
            end_time=datetime.datetime.fromisoformat(data['end_time']) if data['end_time'] else None
        )
        # Set the matchs attribute after the object is created
        round_obj.matchs = [Match.deserialize(match_data) for match_data in data.get('matchs', [])]
        return round_obj
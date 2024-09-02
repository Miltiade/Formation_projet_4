import json
from models.model_tournament import Tournament


def save_tournament_state(tournament, filename="tournament_data.json"):
    serialized_data = tournament.serialize()
    with open(filename, 'w') as f:
        json.dump(serialized_data, f)
    print("Tournament state saved successfully.")

def load_tournament_state(filename="tournament_data.json"):
    with open(filename, 'r') as f:
        serialized_data = json.load(f)
    tournament = Tournament.deserialize(serialized_data)
    print("Tournament state loaded successfully.")
    return 

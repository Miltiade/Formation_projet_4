import json
from models.model_tournament import Tournament

def save_tournament_state(tournament, filename="tournament_data.json"):
    """
    Save the current state of the tournament to a JSON file.
    Args:
        tournament (Tournament): The tournament object to save.
        filename (str): The name of the file to save the tournament state to.
    """
    serialized_data = tournament.serialize()
    with open(filename, 'w') as f:
        json.dump(serialized_data, f)
    print("Tournament state saved successfully.")

def load_tournament_state(filename="tournament_data.json"):
    """
    Load the tournament state from a JSON file.
    Args:
        filename (str): The name of the file to load the tournament state from.
    Returns:
        Tournament: The loaded tournament object.
    """
    with open(filename, 'r') as f:
        serialized_data = json.load(f)
    tournament = Tournament.deserialize(serialized_data)
    print("Tournament state loaded successfully.")
    return 

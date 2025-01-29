# serialize_players.py

import json
from test_data import test_players

# Serialize the list of players
serialized_players = [player.serialize() for player in test_players]

# Save the serialized data to a JSON file
with open("serialized_players.json", "w") as f:
    json.dump(serialized_players, f, indent=4)

print("Players serialized and saved to serialized_players.json")
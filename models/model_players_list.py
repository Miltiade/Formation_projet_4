# Manager of players' list. Responsible for database manipulations

# A class that defines a list of players (and sets up its méthodes + attributs) : add player, delete player, modify player, serialize, deserialize, save_to_database, etc.... modify json file

"""
This module defines the PlayersList class, which is responsible for managing a list of players.

It includes methods for adding, deleting, modifying players, and saving/loading the list to/from a JSON database file.
Classes:
    PlayersList: A class that manages a list of Player objects.
Methods:
    __init__(self):
        Initializes a new instance of the PlayersList class, creating an empty list to store players.
    add_player(self, player):
        Adds a Player object to the players list.
    delete_player(self, player):
        Removes a Player object from the players list.
    modify_player(self, player, new_data):
        Modifies the attributes of a Player object with new data.
    save_all_to_database(self, file_path):
        Saves all Player objects in the players list to a JSON database file.
    load_all_from_database(self, file_path):
        Loads all Player objects from a JSON database file into the players list.
    __str__(self):
        Returns a string representation of the PlayersList object.
    __repr__(self):
        Returns a detailed string representation of the PlayersList object.
    __len__(self):
        Returns the number of Player objects in the players list.
    __getitem__(self, index):
        Gets a Player object by index from the players list.
    __setitem__(self, index, value):
        Sets a Player object at a specific index in the players list.
"""

import json
from models.model_player import Player


class PlayersList:
    # This class is a manager of players
    def __init__(self):
        # Initializes a new instance of the class.
        # This constructor creates an empty list to store players.
        self.players = []

    # This method adds a player to the list
    def add_player(self, player):
        # Adds a player to the players list.
        self.players.append(player)

    def modify_player(self, player, new_data):
        # Modifies the attributes of a player with new data.
        player.family_name = new_data.get("family_name", player.family_name)
        player.first_name = new_data.get("first_name", player.first_name)
        player.date_of_birth = new_data.get("date_of_birth", player.date_of_birth)
        player.elo = new_data.get("elo", player.elo)
        player.initial_ranking = new_data.get("initial_ranking", player.initial_ranking)
        player.match_score = new_data.get("match_score", player.match_score)
        player.total_score = new_data.get("total_score", player.total_score)

    def save_all_to_database(self, file_path):
        # Saves all players to a database file in JSON format.
        players_data = [player.serialize() for player in self.players]
        try:
            with open(file_path, "w") as file:
                json.dump(players_data, file)
        except IOError:
            print("Error while saving players in database.")

    def load_all_from_database(self, file_path):
        # Loads all players from a database file in JSON format.
        try:
            with open(file_path, "r") as file:
                players_data = json.load(file)
                self.players = [Player.from_dict(data) for data in players_data]
        except IOError:
            print("Error while loading players from database.")
        except json.JSONDecodeError:
            print("Error while decoding JSON: cannot read file.")

    def __str__(self):
        # Returns a string representation of the PlayersList object.
        return f"PlayersList({self.players})"

    def __repr__(self):
        # Returns a detailed string representation of the PlayersList object.
        return f"PlayersList({self.players})"

    def __len__(self):
        # Returns the number of players in the list.
        return len(self.players)

    def __getitem__(self, index):
        # Gets a player by index.
        return self.players[index]

    def __setitem__(self, index, value):
        # Sets a player at a specific index.
        self.players[index] = value

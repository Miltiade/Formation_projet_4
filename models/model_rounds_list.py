# model_rounds_list.py
# Manager of rounds' list. Responsible for database manipulations.
# A class that defines a list of rounds (and sets up its méthodes + attributs) : create round, save round to database, load round, etc.... In short: modify json file.

"""
model_rounds_list.py

Manager of rounds' list. Responsible for database manipulations.

This module defines the RoundsList class, which manages a list of rounds and handles
operations such as creating, saving, loading, retrieving, and deleting rounds from a JSON file.

Classes:
    RoundsList: A class that defines a list of rounds and provides methods to manipulate it.

Methods:
    __init__(self, file_path): Initializes the RoundsList with the path to the JSON file and loads existing rounds.
    create_round(self, round_data): Adds a new round to the list and saves the updated list to the file.
    save_rounds(self): Saves the list of rounds to the JSON file.
    load_rounds(self): Loads the list of rounds from the JSON file if it exists, otherwise returns an empty list.
    get_round(self, index): Retrieves a round by its index.
    delete_round(self, index): Deletes a round by its index and saves the updated list to the file.
"""

import json
import os

class RoundsList:
    def __init__(self, file_path):
        # Initialize with the path to the JSON file
        self.file_path = file_path
        # Load existing rounds from the file if it exists
        self.rounds = self.load_rounds()

    def create_round(self, round_data):
        # Add a new round to the list
        self.rounds.append(round_data)
        # Save the updated list to the file
        self.save_rounds()

    def save_rounds(self):
        # Save the list of rounds to the JSON file
        with open(self.file_path, 'w') as file:
            json.dump(self.rounds, file, indent=4)

    def load_rounds(self):
        # Load the list of rounds from the JSON file if it exists
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        # Return an empty list if the file does not exist
        return []

    def get_round(self, index):
        # Retrieve a round by its index
        if 0 <= index < len(self.rounds):
            return self.rounds[index]
        # Return None if the index is out of range
        return None

    def delete_round(self, index):
        # Delete a round by its index
        if 0 <= index < len(self.rounds):
            del self.rounds[index]
            # Save the updated list to the file
            self.save_rounds()
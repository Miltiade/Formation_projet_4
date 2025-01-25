# model_matches_list.py
# Manager of matches' list. Responsible for database manipulations.
# A class that defines a list of matches (and sets up its méthodes + attributs) : create match, save match to database, load match, etc.... In short: modify json file.

"""
model_matches_list.py

This module contains the MatchesList class, which is responsible for managing a list of matches and performing database manipulations. The class provides methods to create, save, load, retrieve, and delete matches from a JSON file.

Classes:
    MatchesList: A class that defines a list of matches and provides methods to manipulate the list.

Methods:
    __init__(self, file_path): Initializes the MatchesList with the given file path and loads the matches from the JSON file.
    create_match(self, match): Adds a new match to the list and saves the updated list to the JSON file.
    save_matches(self): Saves the list of matches to a JSON file.
    load_matches(self): Loads the list of matches from a JSON file.
    get_match(self, match_id): Retrieves a match by its ID.
    delete_match(self, match_id): Deletes a match by its ID and saves the updated list to the JSON file.
"""

import os
import json

class MatchesList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.matches = self.load_matches()

    def create_match(self, match):
        # Add a new match to the list
        self.matches.append(match)
        self.save_matches()

    def save_matches(self):
        # Save the list of matches to a JSON file
        with open(self.file_path, 'w') as file:
            json.dump(self.matches, file, indent=4)

    def load_matches(self):
        # Load the list of matches from a JSON file
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def get_match(self, match_id):
        # Retrieve a match by its ID
        for match in self.matches:
            if match['id'] == match_id:
                return match
        return None

    def delete_match(self, match_id):
        # Delete a match by its ID
        self.matches = [match for match in self.matches if match['id'] != match_id]
        self.save_matches()
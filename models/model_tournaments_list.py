"""
model_tournaments_list.py

Manager of tournaments' list. Responsible for database manipulations.

This module defines the TournamentsList class, which manages a list of tournaments.
It provides methods to create, save, load, update, and delete tournaments from a JSON file.

Classes:
    TournamentsList: A class to manage a list of tournaments.

Methods:
    __init__(self, file_path): Initialize the manager with the path to the JSON file.
    load_tournaments(self): Load tournaments from the JSON file.
    save_tournaments(self): Save the current list of tournaments to the JSON file.
    create_tournament(self, tournament): Add a new tournament to the list and save it.
    get_tournament(self, tournament_id): Retrieve a tournament by its ID.
    update_tournament(self, tournament_id, updated_tournament): Update an existing tournament and save the changes.
    delete_tournament(self, tournament_id): Delete a tournament by its ID and save the changes.
"""

import json
import os

class TournamentsList:
    def __init__(self, file_path):
        # Initialize the manager with the path to the JSON file
        self.file_path = file_path
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        # Load tournaments from the JSON file
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tournaments(self):
        # Save the current list of tournaments to the JSON file
        with open(self.file_path, 'w') as file:
            json.dump(self.tournaments, file, indent=4)

    def create_tournament(self, tournament):
        # Add a new tournament to the list and save it
        self.tournaments.append(tournament)
        self.save_tournaments()

    def get_tournament(self, tournament_id):
        # Retrieve a tournament by its ID
        for tournament in self.tournaments:
            if tournament['id'] == tournament_id:
                return tournament
        return None

    def update_tournament(self, tournament_id, updated_tournament):
        # Update an existing tournament and save the changes
        for index, tournament in enumerate(self.tournaments):
            if tournament['id'] == tournament_id:
                self.tournaments[index] = updated_tournament
                self.save_tournaments()
                return True
        return False

    def delete_tournament(self, tournament_id):
        # Delete a tournament by its ID and save the changes
        self.tournaments = [tournament for tournament in self.tournaments if tournament['id'] != tournament_id]
        self.save_tournaments()


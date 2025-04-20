import os
import json
from tinydb import TinyDB, Query
from models.model_tournament import Tournament
from models.model_player import Player


# Save a single player to the JSON database
def save_player(player):
    # Ensure the directory exists
    os.makedirs("data/tournaments", exist_ok=True)
    # Initialize the TinyDB database
    db = TinyDB("data/tournaments/db.json")
    # Access the 'players' table
    players_table = db.table("players")
    # Serialize the player object
    player_data = player.serialize()
    # Insert the player data into the 'players' table
    players_table.insert(player_data)


# Save new tournament
def save_tournament(tournament):
    db = TinyDB("data/tournaments/db.json")
    tournaments_table = db.table("tournaments")
    tournament_data = tournament.serialize()
    tournaments_table.insert(tournament_data)


# Update (i.e. save) existing tournament in JSON file
def update_tournament(tournament):
    db = TinyDB("data/tournaments/db.json")
    tournaments_table = db.table("tournaments")
    tournament_data = tournament.serialize()
    tournament_query = Query()
    tournaments_table.update(
        tournament_data,
        tournament_query.name == tournament_data["name"]
    )
    print("Tournament updated successfully.")


# Choose and load a tournament
def choose_tournament():
    # Load the tournament data from a JSON file
    with open("data/tournaments/db.json", "r") as file:
        data = json.load(file)
    tournaments = data.get("tournaments", {})
    if not isinstance(tournaments, dict) or not all(
        isinstance(t, dict) for t in tournaments.values()
    ):
        raise ValueError("Invalid data format in tournaments JSON file.")

    # Display the list of tournaments to the user
    for index, (key, tournament) in enumerate(tournaments.items(), start=1):
        print(f"{index}. {tournament['name']}")
    choice = int(input("Enter the number of the tournament you want to load: ")) - 1
    selected_key = list(tournaments.keys())[choice]
    selected_tournament = tournaments[selected_key]

    # Deserialize players into Player objects
    players = {
        player["elo"]: Player.deserialize(player)
        for player in selected_tournament.get("players", [])
    }

    # Pass the players dictionary to Tournament.deserialize
    return Tournament.deserialize(selected_tournament, players)


# Choose and load a player
def choose_player():
    db = TinyDB("data/tournaments/db.json")
    players_table = db.table("players")
    # Fetch all saved players
    saved_players = players_table.all()
    # Check if there are saved players
    if not saved_players:
        print("No saved players found.")
        return None
    # Display the list of players' names
    print("Please choose a player to load:")
    for index, player in enumerate(saved_players):
        print(f"{index + 1}. {player['elo']} - {player['family_name']}")
    # Ask the user to choose a player
    try:
        choice = int(input("Enter the number of the player you want to load: ")) - 1
        if 0 <= choice < len(saved_players):
            selected_player = saved_players[choice]
            print(
                f"You selected player: {selected_player['family_name']} (Elo: {selected_player['elo']})"
            )
            return selected_player
        else:
            print("Invalid selection. Please enter a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


# Create a new player
def create_player():
    family_name = input("Enter the player's family name: ")
    first_name = input("Enter the player's first name: ")
    date_of_birth = input("Enter the player's date of birth (DD-MM-YYYY): ")
    elo = input("Enter the player's ELO: ")
    player = Player(
        family_name,
        first_name,
        date_of_birth,
        elo,
        initial_ranking=0,
        match_score=0,
        total_score=0,
    )
    save_player(player)
    print(f"Player {first_name} {family_name} added successfully.")

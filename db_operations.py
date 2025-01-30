from tinydb import TinyDB, Query
from models.model_tournament import Tournament
from models.model_player import Player

# Save a single player
def save_player(player):
    db = TinyDB('data/tournaments/db.json')
    players_table = db.table('players')
    player_data = player.serialize()
    players_table.insert(player_data)

# Save the tournament
def save_tournament(tournament):
    db = TinyDB('data/tournaments/db.json')
    tournaments_table = db.table('tournaments')
    tournament_data = tournament.serialize()
    tournaments_table.insert(tournament_data)

# Update the tournament (n.b.: use the tournament's name to find the specific tournament)
def update_tournament(tournament):
    db = TinyDB('data/tournaments/db.json')
    tournaments_table = db.table('tournaments')
    tournament_data = tournament.serialize()
    print(tournament_data)
    Tournament = Query()
    tournaments_table.update(tournament_data,Tournament.name==tournament_data["name"])

# Function to choose and load a tournament
def choose_tournament():
    db = TinyDB('data/tournaments/db.json')
    tournaments_table = db.table('tournaments')
    # Fetch all saved tournaments
    saved_tournaments = tournaments_table.all()
    # Check if there are saved tournaments
    if not saved_tournaments:
        print("No saved tournaments found.")
        return None
    # Display the list of tournament names
    print("Please choose a tournament to load:")
    for index, tournament in enumerate(saved_tournaments):
        print(f"{index + 1}. {tournament['name']}")
    # Ask the user to choose a tournament
    try:
        choice = int(input("Enter the number of the tournament you want to load: ")) - 1
        if 0 <= choice < len(saved_tournaments):
            selected_tournament = saved_tournaments[choice]
            print(f"You have selected the tournament: {selected_tournament['name']}")
            return selected_tournament
        else:
            print("Invalid selection. Please enter a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

# Function to choose and load a player
def choose_player():
    db = TinyDB('data/tournaments/db.json')
    players_table = db.table('players')
    # Fetch all saved players
    saved_players = players_table.all()
    # Check if there are saved players
    if not saved_players:
        print("No saved players found.")
        return None
    # Display the list of players' names
    print("Please choose a player to load:")
    for index, player in enumerate(saved_players):
        print(f"{index + 1}. {player['elo']} - {player['name']}")
    # Ask the user to choose a player
    try:
        choice = int(input("Enter the number of the player you want to load: ")) - 1
        if 0 <= choice < len(saved_players):
            selected_player = saved_players[choice]
            print(f"You have selected the player: {selected_player['name']} (Elo: {selected_player['elo']})")
            return selected_player
        else:
            print("Invalid selection. Please enter a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

# Function to add a new player
def add_player():
    family_name = input("Enter the player's family name: ")
    first_name = input("Enter the player's first name: ")
    date_of_birth = input("Enter the player's date of birth (DD-MM-YYYY): ")
    elo = input("Enter the player's ELO: ")
    player = Player(family_name, first_name, date_of_birth, elo,initial_ranking=0, match_score=0, total_score=0)
    save_player(player)
    print(f"Player {first_name} {family_name} added successfully.")

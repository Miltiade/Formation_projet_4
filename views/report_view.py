def list_players_alphabetically():
    players = get_all_players()  # Assuming this function fetches all players from the database
    sorted_players = sorted(players, key=lambda player: player['name'])
    for player in sorted_players:
        print(player['name'])

def list_tournaments():
    tournaments = get_all_tournaments()  # Assuming this function fetches all tournaments from the database
    for tournament in tournaments:
        print(tournament['name'])

def list_tournament_players(tournament_id):
    players = get_tournament_players(tournament_id)  # Assuming this function fetches players for a specific tournament
    for player in players:
        print(player['name'])

def list_tournament_rounds(tournament_id):
    rounds = get_tournament_rounds(tournament_id)  # Assuming this function fetches rounds for a specific tournament
    for round in rounds:
        print(f"Round {round['number']}: {round['name']}")
from controlers.tournament_controler import get_all_players, get_all_tournaments, get_tournament_players, get_tournament_rounds

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

def export_player_list(players, filename="player_list.txt"):
    """Export the list of players to a text file."""
    with open(filename, "w") as file:
        file.write("Player List (Alphabetical Order):\n")
        for player in sorted(players, key=lambda p: p['family_name']):
            file.write(f"{player['family_name']}, {player['first_name']} (ELO: {player['elo']})\n")
    print(f"Player list exported to {filename}.")

def export_tournament_list(tournaments, filename="tournament_list.txt"):
    """Export the list of tournaments to a text file."""
    with open(filename, "w") as file:
        file.write("Tournament List:\n")
        for tournament in tournaments:
            file.write(f"{tournament['name']} - {tournament['start_date']} to {tournament['end_date']}\n")
    print(f"Tournament list exported to {filename}.")

def export_tournament_details(tournament, filename="tournament_details.txt"):
    """Export tournament details to a text file."""
    with open(filename, "w") as file:
        file.write(f"Tournament: {tournament['name']}\n")
        file.write(f"Location: {tournament['place']}\n")
        file.write(f"Dates: {tournament['start_date']} to {tournament['end_date']}\n")
        file.write(f"Description: {tournament['description']}\n")
    print(f"Tournament details exported to {filename}.")

def export_tournament_players(tournament, filename="tournament_players.txt"):
    """Export the list of players in a tournament to a text file."""
    with open(filename, "w") as file:
        file.write(f"Players in Tournament: {tournament['name']} (Alphabetical Order):\n")
        for player in sorted(tournament.players, key=lambda p: p.family_name):
            file.write(f"{player.family_name}, {player.first_name} (ELO: {player.elo})\n")
    print(f"Tournament players exported to {filename}.")

def export_tournament_rounds(tournament, filename="tournament_rounds.txt"):
    """Export the list of rounds and matches in a tournament to a text file."""
    with open(filename, "w") as file:
        file.write(f"Rounds and Matches in Tournament: {tournament['name']}:\n")
        for round_ in tournament.rounds:
            file.write(f"{round_.name}:\n")
            for match in round_.matchs:
                file.write(f"  {match.player1.family_name} vs {match.player2.family_name}\n")
                file.write(f"    Score: {match.score_player1} - {match.score_player2}\n")
    print(f"Tournament rounds exported to {filename}.")
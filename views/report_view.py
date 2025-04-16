import os  # Import os to handle directory creation


def export_player_list(players, filename="player_list.txt"):
    """Export the list of players to a text file."""
    # Ensure the directory exists
    os.makedirs("data/reports", exist_ok=True)
    filepath = os.path.join("data/reports", filename)

    with open(filepath, "w") as file:
        file.write("Player List (Alphabetical Order):\n")
        for player in sorted(players, key=lambda p: p["family_name"]):
            file.write(
                f"{player['family_name']}, {player['first_name']} (ELO: {player['elo']})\n"
            )
    print(f"Player list exported to {filepath}.")


def export_tournament_list(tournaments, filename="tournament_list.txt"):
    """Export the list of tournaments to a text file."""
    # Ensure the directory exists
    os.makedirs("data/reports", exist_ok=True)
    filepath = os.path.join("data/reports", filename)

    with open(filepath, "w") as file:
        file.write("Tournament List:\n")
        for tournament in tournaments:
            file.write(
                f"{tournament['name']} - {tournament['start_date']} to {tournament['end_date']}\n"
            )
    print(f"Tournament list exported to {filepath}.")


def export_tournament_details(tournament, filename="tournament_details.txt"):
    """Export tournament details to a text file."""
    # Ensure the directory exists
    os.makedirs("data/reports", exist_ok=True)
    filepath = os.path.join("data/reports", filename)

    with open(filepath, "w") as file:
        file.write(f"Tournament: {tournament['name']}\n")
        file.write(f"Location: {tournament['place']}\n")
        file.write(f"Dates: {tournament['start_date']} to {tournament['end_date']}\n")
        file.write(f"Description: {tournament['description']}\n")
    print(f"Tournament details exported to {filepath}.")


def export_tournament_players(
    tournament_players,
    tournament_name="Unknown Tournament",
    filename="tournament_players.txt",
):
    """Export the list of players in a tournament to a text file."""
    # Ensure the directory exists
    os.makedirs("data/reports", exist_ok=True)
    filepath = os.path.join("data/reports", filename)

    with open(filepath, "w") as file:
        # Write the tournament name
        file.write(f"Players in Tournament: {tournament_name} (Alphabetical Order):\n")
        # Sort players alphabetically by family name
        for player in sorted(tournament_players, key=lambda p: p["family_name"]):
            file.write(
                f"{player['family_name']}, {player['first_name']} (ELO: {player['elo']})\n"
            )
    print(f"Tournament players exported to {filepath}.")


def export_tournament_rounds(
    tournament_rounds,
    tournament_name="Unknown Tournament",
    filename="tournament_rounds.txt",
):
    """Export the list of rounds and matches in a tournament to a text file."""
    # Ensure the directory exists
    os.makedirs("data/reports", exist_ok=True)
    filepath = os.path.join("data/reports", filename)

    with open(filepath, "w") as file:
        file.write(f"Rounds and Matches in Tournament: {tournament_name}:\n")
        for round_ in tournament_rounds:
            file.write(f"{round_['name']}:\n")
            for match in round_["matches"]:
                file.write(
                    f"  {match['player1']['family_name']} vs {match['player2']['family_name']}\n"
                )
                file.write(
                    f"    Score: {match['score_player1']} - {match['score_player2']}\n"
                )
    print(f"Tournament rounds exported to {filepath}.")

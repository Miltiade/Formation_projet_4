from controlers.tournament_controler import TournamentControler
from models.model_tournament import Tournament
from db_operations import create_player, choose_player, choose_tournament
from views.report_view import (
    export_player_list,
    export_tournament_list,
    export_tournament_details,
    export_tournament_players,
    export_tournament_rounds,
)


def main_menu():
    while True:
        print("0. Exit")
        print("1. Create New Player")
        print("2. Create New Tournament")
        print("3. Load a tournament")  # Load a specific tournament from JSON and run it
        print("4. Add a player to a tournament")
        print("5. Export list of all players in database")
        print("6. Export list of all tournaments in database")
        print("7. Export details of a Tournament")
        print("8. Export players of a Tournament")
        print("9. Export rounds of a tournament -- with matches")

        choice = input("Enter your choice: ")

        if choice == "1":  # Create a new player and save it to JSON
            create_player()

        elif choice == "2":  # Create a new tournament and save it to JSON
            tournamentControler = TournamentControler()
            tournamentControler.create_new_tournament()

        elif choice == "3":  # Load and resume a tournament

            # Prompt the user to choose a saved tournament to resume
            tournament = choose_tournament()  # Load a specific tournament from JSON
            # Validate and deserialize the tournament if necessary
            try:
                if isinstance(tournament, dict):
                    tournament = Tournament.deserialize(tournament)
                elif not isinstance(tournament, Tournament):
                    print("Error: Invalid tournament data. Please try again.")
                    continue
            except Exception as e:
                print(f"Error during deserialization: {e}")
                continue
            # Create a new instance of TournamentControler
            tournamentControler = TournamentControler()
            # If tournament's current_round is 0, call the run_tournament method
            if tournament.current_round == 0:
                tournamentControler.run_tournament(tournament)
            # If tournament's current_round is not 0, call the resume_tournament method
            else:
                tournamentControler.resume_tournament(tournament)

        elif (
            choice == "4"
        ):  # Load a player from JSON to add to a tournament; update tournament in JSON
            tournament = choose_tournament()
            player = choose_player()
            tournamentControler = TournamentControler()
            tournamentControler.add_player_to_tournament(tournament, player)

        elif (
            choice == "5"
        ):  # Export plain text list of all players in "players" section of db.json
            # Create an instance of TournamentControler
            tournamentControler = TournamentControler()
            # Call the get_all_players method
            players = tournamentControler.get_all_players()
            # Export the fetched players
            export_player_list(players)

        elif (
            choice == "6"
        ):  # Export list of all tournaments in "tournaments" section of db.json
            # Create an instance of TournamentControler
            tournamentControler = TournamentControler()
            # Call the get_all_tournaments method
            tournaments = tournamentControler.get_all_tournaments()
            # Export the fetched tournaments
            export_tournament_list(tournaments)

        elif (
            choice == "7"
        ):  # Export plain text list of details for a specific tournament
            # Prompt the user to choose a saved tournament
            tournament = choose_tournament()  # Select a tournament
            # create an instance of TournamentControler
            tournamentControler = TournamentControler()
            # Call the get_tournament_details method
            tournament_details = tournamentControler.get_tournament_details(tournament)
            # Export the fetched tournament details into a text file
            export_tournament_details(tournament_details)

        elif (
            choice == "8"
        ):  # Export plain text list of all players of a specific tournament
            selected_tournament = choose_tournament()  # Select a tournament
            # create an instance of TournamentControler
            tournamentControler = TournamentControler()
            # Call the get_tournament_players method
            tournament_players = tournamentControler.get_tournament_players(
                selected_tournament
            )
            # Export the fetched players into a text file
            export_tournament_players(
                tournament_players, tournament_name=selected_tournament.name
            )

        elif (
            choice == "9"
        ):  # Export plain text list of all rounds of a specific tournament
            selected_tournament = choose_tournament()  # Select a tournament
            if not selected_tournament:
                print("No tournament selected. Returning to main menu.")
                return  # Exit this menu option if no tournament is selected
            # Debugging print to check the type of selected_tournament
            print(f"Type of selected_tournament: {type(selected_tournament)}")
            # Create an instance of TournamentControler
            tournamentControler = TournamentControler()

            # Call the get_tournament_rounds method
            try:  # Fetch all rounds of the selected tournament
                tournament_rounds = tournamentControler.get_tournament_rounds(
                    selected_tournament
                )
            except Exception as e:
                print(f"Error fetching tournament rounds: {e}")
                return  # Exit this menu option if an error occurs

            # Export the fetched rounds into a text file
            try:
                export_tournament_rounds(
                    tournament_rounds, tournament_name=selected_tournament.name
                )
                print("Tournament rounds exported successfully.")  # Debugging print
            except Exception as e:
                print(f"Error exporting tournament rounds: {e}")

        elif choice == "0":  # Exit the program
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()


def list_players_alphabetically(players):
    """
    List players alphabetically by their family name.
    """
    sorted_players = sorted(players, key=lambda x: x.family_name)
    for player in sorted_players:
        print(f"{player.family_name}, {player.first_name}")


def list_tournaments(tournaments):
    """
    List tournaments with their names and dates.
    """
    for tournament in tournaments:
        tournament_name = tournament["name"]
        start_date = tournament["start_date"]
        end_date = tournament["end_date"]
        print(f"{tournament_name} - {start_date} to {end_date}")


def list_tournament_players(tournament):
    """
    List players of a specific tournament alphabetically by their family name.
    """
    sorted_players = sorted(tournament.players, key=lambda x: x.family_name)
    for player in sorted_players:
        print(f"{player.family_name}, {player.first_name}")


def list_tournament_rounds(tournament):
    """
    List rounds of a specific tournament with their matches.
    """
    for round_ in tournament.rounds:
        print(f"{round_.name}")
        for match in round_.matchs:
            print(f"{match.player1.family_name} vs {match.player2.family_name}")

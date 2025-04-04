from controlers.tournament_controler import TournamentControler
from models.model_tournament import Tournament
from db_operations import create_player, choose_player, choose_tournament
from views.report_view import list_players_alphabetically, list_tournaments, list_tournament_players, list_tournament_rounds

def main_menu():
    while True:
        print("1. Create New Player")
        print("2. Create New Tournament")
        print("3. Load Tournament")
        print("4. List Players Alphabetically")
        print("5. List Tournaments")
        print("6. List Tournament Players")
        print("7. List Tournament Rounds")
        print("8. Exit")
        print("9. Add player to tournament")
        print("10. Select and run a tournament")
        choice = input("Enter your choice: ")

        if choice == '1': # Create a new player and save it to JSON
            create_player()

        elif choice == '2': # Create a new tournament and save it to JSON
            tournamentControler = TournamentControler()
            tournamentControler.create_new_tournament()

        elif choice == '3': # Load a specific tournament from JSON
            # tournamentControler = TournamentControler()
            # tournamentControler.load_tournament()
            tournament= choose_tournament()  # Load a specific tournament from JSON
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
            # Resume the tournament: executes all rounds, manages matches, and updates the database
            tournamentControler.run_tournament(tournament)

        elif choice == '4':
            players = choose_player()  # Load a specific player from JSON
            list_players_alphabetically(players)

        elif choice == '5': # List all tournaments
            tournaments = choose_tournament()
            list_tournaments(tournaments)

        elif choice == '6': # List players in a specific tournament
            tournament = choose_tournament()
            list_tournament_players(tournament)

        elif choice == '7': # List rounds in a specific tournament
            tournament = choose_tournament()
            list_tournament_rounds(tournament)

        elif choice == '8': # Exit the program
            break

        elif choice == '9': # Load a specific player from JSON to add to a tournament; update the tournament in JSON
            tournament = choose_tournament()
            player = choose_player()
            tournamentControler = TournamentControler()
            tournamentControler.add_player_to_tournament(tournament,player)

        elif choice == '10':  # Select and run selected tournament
            # Prompt the user to choose a saved tournament to resume
            tournament = choose_tournament()  # Load a specific tournament from JSON.
            # Validate and deserialize the tournament if necessary
            try:
                if isinstance(tournament, dict):  # If the tournament is serialized, deserialize it
                    tournament = Tournament.deserialize(tournament)
                elif not isinstance(tournament, Tournament):  # If not a valid Tournament object, raise an error
                    print("Error: Invalid tournament data. Please try again.")
                    continue
            except Exception as e:
                print(f"Error during deserialization: {e}")
                continue
            # Create a new instance of TournamentControler
            tournamentControler = TournamentControler()
            # Resume the tournament: executes all rounds, manages matches, and updates the database
            tournamentControler.run_tournament(tournament)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

def list_players_alphabetically(players):
    sorted_players = sorted(players, key=lambda x: x.family_name)
    for player in sorted_players:
        print(f"{player.family_name}, {player.first_name}")

def list_tournaments(tournaments):
    for tournament in tournaments:
        print(f"{tournament['name']} - {tournament['start_date']} to {tournament['end_date']}")

def list_tournament_players(tournament):
    sorted_players = sorted(tournament.players, key=lambda x: x.family_name)
    for player in sorted_players:
        print(f"{player.family_name}, {player.first_name}")

def list_tournament_rounds(tournament):
    for round_ in tournament.rounds:
        print(f"{round_.name}")
        for match in round_.matchs:
            print(f"{match.player1.family_name} vs {match.player2.family_name}")


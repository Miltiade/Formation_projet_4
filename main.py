from controlers.tournament_controler import TournamentControler
from db_operations import add_player, choose_player, choose_tournament
from views.report_view import list_players_alphabetically, list_tournaments, list_tournament_players, list_tournament_rounds

def main_menu():
    while True:
        print("1. Add Player")
        print("2. Create New Tournament")
        print("3. Load Tournament")
        print("4. List Players Alphabetically")
        print("5. List Tournaments")
        print("6. List Tournament Players")
        print("7. List Tournament Rounds")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_player()
        elif choice == '2':
            tournamentControler = TournamentControler()
            tournamentControler.create_new_tournament()
            print("TOURNAMENT CREATED!")
            tournamentControler.print_player()
            print("PLAYERS' LIST PRINTED!")
            tournamentControler.run_first_round()
            print("ROUND 1 RUN SUCCESSFULLY!")
            tournamentControler.run_subsequent_rounds()
            print("ALL ROUNDS RUN SUCCESSFULLY!")
            tournamentControler.display_final_ranking()
            print("FINAL RANKING DISPLAYED SUCCESSFULLY!")
        elif choice == '3':
            tournamentControler = TournamentControler()
            tournamentControler.load_tournament()
        elif choice == '4':
            players = choose_player()  # Implement this function to load a specific player from JSON
            list_players_alphabetically(players)
        elif choice == '5':
            tournaments = choose_tournament()  # Implement this function to load a specific tournament from JSON
            list_tournaments(tournaments)
        elif choice == '6':
            tournament = choose_tournament()  # Implement this function to load a specific tournament from JSON
            list_tournament_players(tournament)
        elif choice == '7':
            tournament = choose_tournament()  # Implement this function to load a specific tournament from JSON
            list_tournament_rounds(tournament)
        elif choice == '8':
            break
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
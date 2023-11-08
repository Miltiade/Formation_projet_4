from tinydb import TinyDB, Query

db = TinyDB('db.json')
tournaments_table = db.table('tournaments')

def save_tournament(tournament):
    tournament_data = tournament.serialize()
    print(tournament_data)
    tournaments_table.insert(tournament_data)

def update_tournament(tournament):
    tournament_data = tournament.serialize()
    print(tournament_data)
    Tournament = Query()
    tournaments_table.update(tournament_data,Tournament.name==tournament_data["name"])


def choose_tournament():
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
    
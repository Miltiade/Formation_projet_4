from models import model_tournament,model_round,model_match
from views import tournament_view,round_view,match_view,player_view
from db_operations import save_tournament,update_tournament,choose_tournament
from tests.test_data import test_players,test_tournament
from models.model_player import Player

class TournamentControler:
    def __init__(self):
        self.tournament = test_tournament
        self.players = test_players

    def create_new_tournament(self):
        print("Creating new tournament. Please wait...")
        name = self.get_letters("Enter the tournament's name : ")
        place = self.get_letters("Enter the tournament's place :")
        start_date = self.get_date("Enter the tournament's start date : ")
        end_date = self.get_date("Enter the tournament's end date : ")
        time_control = self.get_time_control()
        description = self.get_letters("Enter a description or comment of this tournament (optional): ")
        number_of_rounds = self.get_numbers("How many rounds shall this tournament have? Enter a number: ")
        print("Creating new tournament. Please wait...")
        # name = test_tournament_data["name"]
        # place = test_tournament_data["place"]
        # start_date = test_tournament_data["start_date"]
        # end_date = test_tournament_data["end_date"]
        # time_control = test_tournament_data["time_control"]
        # description = test_tournament_data["description"]
        # players = []
        # number_of_rounds = test_tournament_data["number_of_rounds"]
        # current_round = test_tournament_data["current_round"]
        # self.tournament = model_tournament.Tournament(name, place, start_date, end_date, time_control, description, test_players)
        print("Tournament created.")
        # for i in range(8):
        #     name, elo = player_view.get_player_info()
        #     player = model_player.Player(name, elo)
        #     self.tournament.add_player(player)
        print("Tournament created.")

    def get_letters(self, message):
        word = tournament_view.get_user_input(message)
        while not word.isalpha():
            tournament_view.error_message("Error: type letters only")
            word = tournament_view.get_user_input(message)
        return word

    def get_time_control(self):
        message = "Enter time control (Bullet/Splitz/Quick) : "
        time_control = tournament_view.get_user_input(message)
        while not time_control.lower() in ["bullet", "splitz", "quick"]:
            tournament_view.error_message("Error: type a valid time control")
            time_control = tournament_view.get_user_input(message)
        return time_control

    def get_date(self,message):
        date = tournament_view.get_user_input(message)
        while not date.isdecimal() and not date.__len__(8):
            tournament_view.error_message("Error : type a date as DDMMYYYY")
            date = tournament_view.get_user_input(message)
        return date

    def get_numbers(self,message):
        number = tournament_view.get_user_input(message)
        while not number.isnumeric():
            tournament_view.error_message("Error: type a number only")
            number = tournament_view.get_user_input(message)
        return number


    def print_player(self):
        players = [Player.from_dict(data) for data in self.tournament.player_elos]
        player_view.print_player(players)

    def run_first_round(self):
        # algorithm running the first round
        print("Starting to run round 1.")
        self.tournament.player_elos.sort(key = lambda x : -x.elo) # sorting players by elo, from highest elo to lowest elo
        for rank, player in enumerate(self.tournament.player_elos, start=1):
            player.initial_ranking = rank
        round1 = model_round.Round("1") # creating object "first round" and declaring it as variable
        self.tournament.add_round(round1) # adding the variable in the tournament
        for i in range(0, len(self.tournament.player_elos), 2): # adding matches in the round
            new_match = model_match.Match(self.tournament.player_elos[i], self.tournament.player_elos[i + 1])
            round1.add_match(new_match)
            

        for match in self.tournament.rounds[0].matchs: # for all matches: add scores & print results
            print(match.player1)
            print(match.player2)
            self.tournament.matches_played.append((match.player1, match.player2)) # update the tournament's matches_played list with the players of the current match
            match.score_player1,match.score_player2 = self.handle_score()
            match.player1.total_score += match.score_player1
            match.player2.total_score += match.score_player2
            match_view.print_match_result(match)
        
        save_tournament(self.tournament)
        print(f"Round finished; tournament state has been saved.")


    def handle_score(self):
        score = match_view.enter_match_result()
        if(score == "1"):
            return 1,0
        elif(score == "2"):
            return 0,1
        else:
            return 0.5,0.5


    def generate_pairs(self):
        """
        Generates pairs of players for the next round of the tournament.
        :param self.tournament: The tournament object containing the list of players and their scores.
        :return: List of pairs (matches) for the next round.
        """
        print("Generating pairs. Please wait...")
        # Sort players based on their scores
        sorted_players = sorted(self.tournament.player_elos, key=lambda x: (-x.total_score, x.initial_ranking))
        print("players sorted")

        matches = []  # List to hold the matches for the next round.
        used_players = set()  # Set of players already paired for this round.

        for i in range(len(sorted_players)):
            if sorted_players[i] not in used_players:
                for j in range(i+1, len(sorted_players)):
                    # Look for a player the current player hasn't played against and is not yet used in this round.
                    if (sorted_players[j] not in used_players and
                            not self.has_played_against(sorted_players[i], sorted_players[j])):
                        
                        matches.append((sorted_players[i], sorted_players[j]))
                        used_players.add(sorted_players[i])
                        used_players.add(sorted_players[j])
                        break  # Break out of the inner loop once we've found a match for the current player.

        return matches


    def has_played_against(self,player1, player2):
        """
        Checks if two players have played against each other in the tournament.
        
        :param player1: First player object.
        :param player2: Second player object.
        :return: True if they've played against each other, False otherwise.
        """
        for match in self.tournament.matches_played:
            if (match[0] == player1 and match[1] == player2) or (match[0] == player2 and match[1] == player1):
                return True
        return False

    def run_subsequent_rounds(self):
        """
        Runs each round after the first one until the tournament is completed.
        """
        # tournament_data = tournament.serialize()
        # self.tournament = None
        # self.deserializer(tournament_data)
        number_of_rounds = self.tournament.number_of_rounds

        for round_number in range(2, number_of_rounds + 1):
            print(f"Starting to run round {round_number}.")

            # Create a new round object
            current_round = model_round.Round(str(round_number))
            self.tournament.add_round(current_round)

            # Generate pairs for the current round
            pairs = self.generate_pairs()
            
            # Add matches to the current round
            for player1, player2 in pairs:
                new_match = model_match.Match(player1, player2)
                current_round.add_match(new_match)
                self.tournament.matches_played.append((player1, player2))  # Update the tournament's matches_played list

            # Run the matches for the current round
            for match in current_round.matchs:
                print(match.player1)
                print(match.player2)
                match.score_player1, match.score_player2 = self.handle_score()
                match.player1.total_score += match.score_player1
                match.player2.total_score += match.score_player2
                match_view.print_match_result(match)

            print(f"Round {round_number} completed.")
            
            update_tournament(self.tournament)
            print(f"Round {round_number} has finished. Tournament state has been saved.")


        print("Tournament completed.")

    def display_final_ranking(self):
        """
        Displays the final ranking of all players at the end of the tournament.
        """
        print("printing Final Ranking of Players...")
        # If player_elos contains serialized dictionaries, use dictionary keys
        sorted_players = sorted(self.tournament.player_elos, key=lambda x: (-x['total_score'], x['initial_ranking']))
        for rank, player in enumerate(sorted_players, start=1):
            print(f"Final Ranking of Players: {rank}. {player['family name']} {player['first name']} - Total Score: {player['total_score']} points")

    def load_tournament(self):
        tournament_data = choose_tournament()
        if tournament_data:
            # Deserialize the tournament data back into a Tournament object
            tournament = model_tournament.Tournament.deserialize(self,tournament_data)
            print(f"Tournament '{tournament.name}' loaded successfully.")
            return tournament
        else:
            print("Tournament loading cancelled.")
            return None

def get_all_players():
    # Fetch all players from the database
    return [
        {'name': 'Alice'},
        {'name': 'Bob'},
        {'name': 'Charlie'}
    ]

def get_all_tournaments():
    # Fetch all tournaments from the database
    return [
        {'name': 'Tournament 1'},
        {'name': 'Tournament 2'}
    ]

def get_tournament_players(tournament_id):
    # Fetch players for a specific tournament from the database
    return [
        {'name': 'Alice'},
        {'name': 'Bob'}
    ]

def get_tournament_rounds(tournament_id):
    # Fetch rounds for a specific tournament from the database
    return [
        {'number': 1, 'name': 'Round 1'},
        {'number': 2, 'name': 'Round 2'}
    ]

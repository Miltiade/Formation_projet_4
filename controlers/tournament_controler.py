from models.model_player import Player
from views import tournament_view, match_view, player_view
from db_operations import update_tournament, choose_tournament, save_tournament
import models.model_tournament as model_tournament  # Import model_tournament module
import models.model_round as model_round  # Import model_round module
import models.model_match as model_match  # Import model_match module

class TournamentControler:
    def __init__(self):
        self.tournament = None
        self.players = []

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
        # Create a new tournament instance
        self.tournament = model_tournament.Tournament(name, place, start_date, end_date, time_control, description, self.players, number_of_rounds,0,[],[])
        print("Tournament created.")
        # Save tournament to database
        save_tournament(self.tournament)
    
        # for i in range(2):
        #     name, elo = player_view.get_player_info()
        #     player = model_player.Player(name, elo)
        #     self.tournament.add_player(player)

    def get_letters(self, message):
        word = tournament_view.get_user_input(message)
        # while not word.isalpha():
        #     tournament_view.error_message("Error: type letters only")
        #     word = tournament_view.get_user_input(message)
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
        while not date.isdecimal() or len(date) != 8:
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
        # Algorithm running the first round
        print("Starting to run round 1.")
        print(self.tournament.player_elos)
        print("Sorting players by elo.")
        
        # Sort player elos by the numeric part of each string, from highest to lowest
        self.tournament.player_elos.sort(key=lambda x: -int(''.join(filter(str.isdigit, x))))
        print(self.tournament.player_elos)
        
        # Update the initial_ranking of the corresponding player objects
        for rank, elo in enumerate(self.tournament.player_elos, start=1):
            for player in self.tournament.players:
                if player.elo == elo:
                    player.initial_ranking = rank
                    break
        print("Players sorted.")
        
        round1 = model_round.Round("1")  # Creating object "first round" and declaring it as variable
        self.tournament.add_round(round1)  # Adding the variable in the tournament
        
        for i in range(0, len(self.tournament.player_elos), 2):  # Adding matches in the round
            # Find the player objects corresponding to the elos
            player1 = next(player for player in self.tournament.players if player.elo == self.tournament.player_elos[i])
            player2 = next(player for player in self.tournament.players if player.elo == self.tournament.player_elos[i + 1])
            new_match = model_match.Match(player1, player2)
            round1.add_match(new_match)
            
        
        print("Running matches for round 1.")
        for match in self.tournament.rounds[0].matchs:  # For all matches: add scores & print results
            # self.tournament.matches_played.append((match.player1, match.player2))  # Update the tournament's matches_played list with the players of the current match
            match.score_player1, match.score_player2 = self.handle_score()  # Add scores to the match
            match.player1.total_score += match.score_player1 # Update the total score of player1
            match.player2.total_score += match.score_player2 # Update the total score of player2
            match_view.print_match_result(match) # Print the result of the match
        print("Round 1 finished.")
        update_tournament(self.tournament) # Update the tournament in the database
        print("Tournament updated.")

    def handle_score(self):
        while True:
            score = match_view.enter_match_result()
            if score == "1":
                return 1, 0
            elif score == "2":
                return 0, 1
            elif score == "0":
                return 0.5, 0.5
            else:
                print("Invalid input. Please try again.")


    def generate_pairs(self):
        """
        Generates pairs of players for the next round of the tournament.
        :param self.tournament: The tournament object containing the list of players and their scores.
        :return: List of pairs (matches) for the next round.
        """
        print("Generating pairs of players based on their score.")
        # Sort players based on their scores
        sorted_players = sorted(self.tournament.player_elos, key=lambda x: (-x.total_score, x.initial_ranking))
        print("Players sorted.")

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
        # Ensure number_of_rounds is an integer
        number_of_rounds = int(self.tournament.number_of_rounds)
        
        for round_number in range(2, number_of_rounds + 1):
            print(f"Starting to run round {round_number}.")
            
            # Create a new round object
            round_ = model_round.Round(str(round_number))
            self.tournament.add_round(round_)
            
            for i in range(0, len(self.tournament.player_elos), 2):  # Adding matches in the round
                # Find the player objects corresponding to the elos
                player1 = next(player for player in self.tournament.players if player.elo == self.tournament.player_elos[i])
                player2 = next(player for player in self.tournament.players if player.elo == self.tournament.player_elos[i + 1])
                new_match = model_match.Match(player1, player2)
                round_.add_match(new_match)
            
            print(f"Running matches for round {round_number}.")
            for match in round_.matchs:  # For all matches: add scores & print results
                self.tournament.matches_played.append((match.player1, match.player2))  # Update the tournament's matches_played list with the players of the current match
                match.score_player1, match.score_player2 = self.handle_score()  # Add scores to the match
                match.player1.total_score += match.score_player1 # Update the total score of player1
                match.player2.total_score += match.score_player2 # Update the total score of player2
                match_view.print_match_result(match) # Print the result of the match
            
            print(f"Round {round_number} finished.")
            update_tournament(self.tournament)  # Update the tournament in the database
            print("Tournament updated.")

    def display_final_ranking(self):
        """
        Displays the final ranking of all players at the end of the tournament.
        """
        print("printing Final Ranking of Players...")
        # If player_elos contains serialized dictionaries, use dictionary keys
        print(self.tournament.player_elos)
        print('total_score')
        sorted_players = sorted(self.tournament.player_elos, key=lambda x: (-x['total_score'], x['initial_ranking']))
        for rank, player in enumerate(sorted_players, start=1):
            print(f"Final Ranking of Players: {rank}. {player['family name']} {player['first name']} - Total Score: {player['total_score']} points")

    def load_tournament(self):
        tournament_data = choose_tournament()
        if tournament_data:
            # Deserialize the tournament data back into a Tournament object
            tournament = model_tournament.Tournament.deserialize(tournament_data)
            print(f"Tournament '{tournament.name}' loaded successfully.")
            return tournament
        else:
            print("Tournament loading cancelled.")
            return None

    def add_player_to_tournament(self, tournament, player):
        """
        Add an existing player to a tournament.
        
        Args:
        tournament (Tournament): The tournament to which the player will be added.
        player (dict or Player): The player to be added to the tournament.
        
        Returns:
        bool: True if the player was added successfully, False otherwise.
        """
        if not isinstance(tournament, model_tournament.Tournament):
            # Deserialize the tournament if it's not already a Tournament object
            tournament = model_tournament.Tournament.deserialize(tournament)
        
        # Ensure player is an instance of Player
        if isinstance(player, dict):
            player = Player.from_dict(player)
        
        # Check if the player is already in the tournament
        if player.serialize() not in [p.serialize() for p in tournament.players]:
            tournament.add_player(player)  # Use the add_player method
            # Save the updated tournament data to the database
            update_tournament(tournament)
            print(f"Player {player.family_name} added to tournament {tournament.name}.")
            return True
        else:
            print(f"Player {player.family_name} is already in tournament {tournament.name}.")
            return False
        
    def run_tournament(self, tournament):
        """
        Run a tournament from the first round to the final round: generate pairs, run matches, and update the database (save).
        
        Args:
        tournament (Tournament): The tournament to be run.
        """
        # if not isinstance(tournament, model_tournament.Tournament):
            # Deserialize the tournament if it's not already a Tournament object
            # tournament = model_tournament.Tournament.deserialize(tournament)
        self.tournament = tournament
        print(self.tournament.player_elos)
        self.run_first_round()
        self.run_subsequent_rounds()
        self.display_final_ranking()
        print("Tournament finished.")


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

from models import model_tournament,model_round,model_match,model_player
from views import tournament_view,round_view,match_view,player_view

class TournamentControler:
    def __init__(self):
        self.tournament = None

    def create_new_tournament(self):
        # name = self.get_letters("Enter the tournament's name : ")
        # place = self.get_letters("Enter the tournament's place :")
        # start_date = self.get_date("Enter the tournament's start date : ")
        # end_date = self.get_date("Enter the tournament's end date : ")
        # time_control = self.get_time_control()
        # description = self.get_letters("Enter a description or comment of this tournament (optional): ")
        # number_round = self.get_numbers("How many rounds this tournament will have? Enter a number: ")
        name = "tournoi"
        place = "paris"
        start_date = "01-01-2023"
        end_date = "02-01-2023"
        time_control = "Bullet"
        description = "random"
        players = [
            model_player.Player("Ranga", 34),
            model_player.Player("Grégory", 12),
            model_player.Player("Jean-Marie", 3),
            model_player.Player("toto", 100),
            model_player.Player("John", 4),
            model_player.Player("Rita", 15),
            model_player.Player("Severus", 56),
            model_player.Player("Padfoot", 50)]
        number_round = 4
        current_round = 0
        self.tournament = model_tournament.Tournament(name, place, start_date, end_date, time_control, description, players, number_round, current_round)
        # for i in range(8):
        #     name, elo = player_view.get_player_info()
        #     player = model_player.Player(name, elo)
        #     self.tournament.add_player(player)

    def get_letters(self, message):
        word = tournament_view.get_user_input(message)
        while not word.isalpha():
            tournament_view.error_message("Erreur de saisie : Entrez uniquement des lettres")
            word = tournament_view.get_user_input(message)
        return word

    def get_time_control(self):
        message = "Enter time control (Bullet/Splitz/Quick) : "
        time_control = tournament_view.get_user_input(message)
        while not time_control.lower() in ["bullet", "splitz", "quick"]:
            tournament_view.error_message("Error de saisie : Entrez un time controle valide")
            time_control = tournament_view.get_user_input(message)
        return time_control

    def get_date(self,message):
        date = tournament_view.get_user_input(message)
        while not date.isdecimal() and not date.__len__(8): # tant que la date saisie n'est pas un nombre et qu'elle n'est pas un string de 8 caractères
            tournament_view.error_message("Erreur de saisie : Entrez une date au format JJMMAAAA")
            date = tournament_view.get_user_input(message)
        return date

    def get_numbers(self,message):
        number = tournament_view.get_user_input(message)
        while not number.isnumeric():
            tournament_view.error_message("Erreur de saisie : Entrez uniquement un nombre")
            number = tournament_view.get_user_input(message)
        return number

    def print_player(self):
        player_view.print_player(self.tournament.players)

    def run_first_round(self):
        # algorithm running the first round
        print("Starting to run first round.")
        self.tournament.players.sort(key = lambda x : x.elo) # sorting players by elo
        round1 = model_round.Round("1") # creating object "first round" and declaring it as variable
        self.tournament.add_round(round1) # adding the variable in the tournament
        for i in range(2): # adding matches in the round
            new_match = model_match.Match(self.tournament.players[i], self.tournament.players[2 + i])
            round1.add_match(new_match)
        print("matches added!",round1) # debugging print; POURQUOI IL NE PRINTE PAS LA LISTE DES MATCHES DU ROUND?
            
        for match in self.tournament.rounds[0].matchs: # for all matches: add scores & print results
            """print(match.player1)
            print(match.player2)"""
            match.score_player1, match.score_player2 = self.handle_score()
            match_view.print_match_result(match)

    def handle_score(self):
        score = match_view.enter_score()
        if(score == "1"):
            return 1,0
        elif(score == "2"):
            return 0,1
        else:
            return 0.5,0.5
    
    def generate_pairs(self): # POURQUOI quand l'argument est self.tournament l'IDE y voit une erreur ?
        """
        Generates pairs of players for the next round of the tournament.
        :param self.tournament: The tournament object containing the list of players and their scores.
        :return: List of pairs (matches) for the next round.
        """
        # Sort players based on their scores
        sorted_players = sorted(self.tournament.players, key=lambda x: (-x.score, x.initial_ranking))
        print(sorted_players,"players sorted")

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
        print(matches) # pourquoi il ne veut pas printer les matches alors qu'il est mentionné une ligne avant ?
    # print("matches created!") # debugging print


    def has_played_against(player1, player2):
        """
        Checks if two players have played against each other in the tournament.
        
        :param player1: First player object.
        :param player2: Second player object.
        :return: True if they've played against each other, False otherwise.
        """
        for match in player1.matches_played:
            if match.opponent == player2:
                return True
        return False
        print("verified has_played_against") #debugging print


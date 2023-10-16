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
        #algorithme pour créer les premiers rounds
        self.tournament.players.sort(key = lambda x : x.elo)
        round1 = model_round.Round("1")
        self.tournament.add_round(round1)
        for i in range(2):
            new_match = model_match.Match(self.tournament.players[i], self.tournament.players[2 + i])
            round1.add_match(new_match)
            
    #     for match in self.tournament.rounds[0].matchs:
    #         """print(match.player1)
    #         print(match.player2)"""
    #         match.score_player1, match.score_player2 = self.handle_score()
    #         match_view.print_match_result(match)

    # def handle_score(self):
    #     score = match_view.enter_score()
    #     if(score == "1"):
    #         return 1,0
    #     elif(score == "2"):
    #         return 0,1
    #     else:
    #         return 0.5,0.5
        

    # def get_ine(self):
    #     message = "Enter the club's INE: "
    #     ine = tournament_view.get_user_input(message)
    #     while ine != "AB12345":
    #         tournament_view.error_message("Erreur de saisie : ceci n'est pas l'INE du club. Réessayez.")
    #         ine = tournament_view.get_user_input(message)
    #     return ine


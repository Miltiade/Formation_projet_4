import models.models as models
import views.views as views

########### NB: REVISER __init__.py ET LES IMPORTS EN PYTHON ##############

# players = [Player("Ranga", 34), Player("Grégory", 12), Player("Jean-Marie", 3), Player("toto", 100)]

class TournamentControler:
    def __init__(self):
        self.tournament = None

    def create_new_tournament(self):
        name = self.get_letters("Enter the tournament name : ")
        time_control = self.get_time_control()
        self.tournament = models.Tournament(name, time_control) 
        #################### L'UTILISATEUR DOIT SAISIR LES AUTRES DONNEES #######################
        # self.tournament = Tournament("Paris", "Bullet")
        """for i in range(8):
            name, elo = get_player_info()
            player = Player(name, elo)
            self.tournament.add_player(player)"""
        # self.tournament.players = players

    def get_letters(self, message):
        word = views.get_user_input(message)
        while not word.isalpha():
            error_message("Erreur de saisie : Entrez uniquement des lettres")
            word = get_user_input(message)
        return word

    def get_numbers ########## L'UTILISATEUR DOIT SAISIR... ###########

    def get_time_control(self):
        message = "Enter time control (Bullet/Splitz/Quick) : "
        time_control = get_user_input(message)
        while not time_control.lower() in ["bullet", "splitz", "quick"]:
            error_message("Error de saisie : Entrez un time controle valide")
            time_control = get_user_input(message)
        return time_control
            
    def print_player(self):
        print_player(self.tournament.players)
        
    def run_first_round(self):
        #algorithme pour créer les premiers rounds
        self.tournament.players.sort(key = lambda x : x.elo)
        round1 = Round("1")
        self.tournament.add_round(round1)
        for i in range(2):
            round1.add_match(self.tournament.players[i], self.tournament.players[2 + i])
            
        for match in self.tournament.rounds[0].matchs:
            """print(match.player1)
            print(match.player2)"""
            match.score_player1, match.score_player2 = self.handle_score()
            print_match_result(match)
            
            
    def handle_score(self):
        score = enter_score()
        if(score == "1"):
            return 1,0
        elif(score == "2"):
            return 0,1
        else:
            return 0.5,0.5
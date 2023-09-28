import datetime

#--------------------------------------------       
class Tournament:
    def __init__(self, ine, name, place, start_date, end_date, current_round, time_control, description, number_round=4):
        self.ine = ine #identifiant_national_dechecs
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_round = number_round
        self.current_round = current_round
        self.players = []
        self.rounds = []
        self.description = description
        self.time_control = time_control
        
    def add_player(self, player):
        self.players.append(player)
        
    def add_round(self, round):
        self.rounds.append(round)
#-----------------------------------------------------  
class Player:
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
        
    def __str__(self):
        return f"{self.name} | {self.elo}"

#-----------------------------------------------------
class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
        self = ([player1,score_player1],[player2,score_player2]) # Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, 
                                                                # chacune contenant deux éléments : un joueur et un score
        
#Victoire 1 points 0 pour l'autre
#Match nul 0.5 pour les deux

#-----------------------------------------------------
class Round:
    def __init__(self, number, name=None, start_time= None, end_time=None):
        self.matchs = []
        self.number = number
        if name is None:
            self.name = "Round " + str(number)
        else:
            self.name = name # Pourquoi on ne peut pas mettre ces 4 lignes directement dans les attributs du innit ?
        self.start_time=start_time
        self.end_time=end_time
        
    def add_match(self, match):
        self.matchs.append(match)

    def create(self):
        # Set the start time when the round is created
        self.start_time = datetime.datetime.now()

    def mark_as_completed(self):
        # Set the end time when the round is marked as completed
        self.end_time = datetime.datetime.now()

    # def set_start_time(self, start_time):
    #     # Set the start time explicitly
    #     if start_time is None:
    #         start_time = datetime.datetime.now()
    # def set_end_time(self, end_time):
    #     # Set the end time explicitly
    #      if end_time is None:
    #         end_time = datetime.datetime.now()


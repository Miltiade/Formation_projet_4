#-------------------MODEL---------------------       
class Tournament:
    def __init__(self, name, time_control, number_round = 4):
        self.name = name
        self.time_control = time_control
        self.number_round = number_round
        self.players = []
        self.rounds = []
        
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
        
#Victoire 1 points 0 pour l'autre
#Match nul 0.5 pour les deux

#-----------------------------------------------------
class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []
        
    def add_match(self, player1, player2): #1
        match = Match(player1, player2)
        self.matchs.append(match)
        
    def add_match2(self, match): #2
        self.matchs.append(match)

class Tournament:
    def __init__(self, ine, name, place, start_date, end_date, time_control, description, number_round=4, current_round=0):
        self.ine = ine
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_round = number_round
        self.description = description
        self.time_control = time_control
        self.current_round = current_round
        self.players = []
        self.rounds = []
        
    def add_player(self, player):
        self.players.append(player)
        
    def add_round(self, round):
        self.rounds.append(round)
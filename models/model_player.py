class Player:
    def __init__(self, name, elo, initial_ranking=0, match_score=0, total_score=0):
        self.name = name
        self.elo = elo
        self.match_score = match_score # player's score in the current match
        self.total_score = total_score # player's total score at a given time
        self.initial_ranking = initial_ranking
        
    def __str__(self):
        return f"{self.name} | {self.elo} |{self.initial_ranking} | {self.match_score} | {self.total_score}"
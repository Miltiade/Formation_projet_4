

class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        from models.model_player import Player  # Import here to avoid circular imports
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def serialize(self):
        # Serialize the match object to a dictionary
        return {
            'player1': self.player1.serialize(),
            'player2': self.player2.serialize(),
            'score_player1': self.score_player1,
            'score_player2': self.score_player2,
        }

    @classmethod
    def deserialize(cls, data):
        # Deserialize the match object from a dictionary
        return cls(
            player1=Player.deserialize(data['player1']),
            player2=Player.deserialize(data['player2']),
            score_player1=data['score_player1'],
            score_player2=data['score_player2']
        )
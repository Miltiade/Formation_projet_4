class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def serialize(self):
        return {
            'player1': self.player1.elo,
            'player2': self.player2.elo,
            'score_player1': self.score_player1,
            'score_player2': self.score_player2
        }

    @classmethod
    def deserialize(cls, data, players):
        player1 = next(player for player in players if player.elo == data['player1'])
        player2 = next(player for player in players if player.elo == data['player2'])
        return cls(
            player1=player1,
            player2=player2,
            score_player1=data['score_player1'],
            score_player2=data['score_player2']
        )
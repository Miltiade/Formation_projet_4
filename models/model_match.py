class Match:
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def serialize(self):
        """
        Serializes the match to a dictionary.
        :return: Dictionary containing match data.
        """
        return {
            "player1": self.player1.elo,
            "player2": self.player2.elo,
            "score_player1": self.score_player1,
            "score_player2": self.score_player2,
        }

    @staticmethod
    def deserialize(data, players):
        """
        Deserializes a match from a dictionary.

        :param data: Dictionary containing match data.
        :param players: Dictionary of all players, keyed by their ELO.
        :return: A Match object.
        """
        # Resolve player1 and player2 using their ELOs
        player1 = players.get(data["player1"])  # Use the ELO to get the Player object
        player2 = players.get(data["player2"])  # Use the ELO to get the Player object

        # Check if players exist
        # If players are not found, raise an error
        if not player1 or not player2:
            raise ValueError(
                f"Player data not found for ELOs: {data['player1']}, {data['player2']}"
            )

        # Create and return the Match object
        return Match(
            player1=player1,
            player2=player2,
            score_player1=data["score_player1"],
            score_player2=data["score_player2"],
        )

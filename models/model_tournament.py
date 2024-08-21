from models import model_round,model_match,model_player

class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description, player_elos=[], number_of_rounds=4, current_round=0):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.player_elos = player_elos # what is stored is: player's elos, not player themselves
        self.time_control = time_control
        self.current_round = current_round
        self.rounds = []
        self.matches_played = []

    def add_player(self, player):
        self.players.append(player)
        
    def add_round(self, round):
        self.rounds.append(round)

    def serialize(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'number_of_rounds': self.number_of_rounds,
            'description': self.description,
            'player_elos': self.player_elos,
            'time_control': self.time_control,
            'current_round': self.current_round,
            'rounds': [round_.serialize() for round_ in self.rounds],
            'matches_played': [(p1_elo, p2_elo) for p1_elo, p2_elo in self.matches_played]
        }

    @staticmethod
    def deserialize(tournament_data, player_objects):
        # This assumes player_objects is a dict mapping player elos to player objects
        tournament = Tournament(
            tournament_data['name'], tournament_data['place'],
            tournament_data['start_date'], tournament_data['end_date'],
            tournament_data['time_control'], tournament_data['description'],
            player_elos=tournament_data['player_elos'],
            number_of_rounds=tournament_data['number_of_rounds'],
            current_round=tournament_data['current_round']
        )
        tournament.players = [player_objects[elo] for elo in tournament_data['player_elos']]
        tournament.rounds = [model_round.Round.deserialize(round_) for round_ in tournament_data['rounds']]
        tournament.matches_played = [
            (player_objects[p1_elo], player_objects[p2_elo])
            for p1_elo, p2_elo in tournament_data['matches_played']
        ]
        return tournament
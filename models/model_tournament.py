from models import model_round,model_match,model_player

class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description, player_elos, number_of_rounds, current_round, rounds, matches_played):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.player_elos = player_elos
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.rounds = rounds
        self.matches_played = matches_played

    def add_player(self, player):
        self.players.append(player)
        # Update player_elos whenever a player is added
        self.player_elos.append(player.serialize())

    def add_round(self, round):
        self.rounds.append(round)

    def serialize(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_rounds': self.number_of_rounds,
            'description': self.description,
            'player_elos': self.player_elos,
            'time_control': self.time_control,
            'current_round': self.current_round,
            'rounds': self.rounds,
            'matches_played': self.matches_played
        }

    @staticmethod
    def deserialize(tournament_data):
        return Tournament(
            tournament_data['name'],
            tournament_data['place'],
            tournament_data['start_date'],
            tournament_data['end_date'],
            tournament_data['time_control'],
            tournament_data['description'],
            tournament_data['player_elos'],
            tournament_data['number_of_rounds'],
            tournament_data['current_round'],
            tournament_data['rounds'],
            tournament_data['matches_played']
        )
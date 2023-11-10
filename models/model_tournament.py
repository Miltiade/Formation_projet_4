from models import model_round,model_match,model_player

class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description, players=[], number_of_rounds=4, current_round=0):

        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.players = players
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
            'players': [player.serialize() for player in self.players],
            'time_control': self.time_control,
            'current_round': self.current_round,
            'rounds': [round_.serialize() for round_ in self.rounds],
            'matches_played': [(player1.serialize(), player2.serialize()) for player1, player2 in self.matches_played]
        }

    def deserialize(self,tournament_data,start_date,end_date,time_control,description):
        self.tournament = Tournament(tournament_data["name"], tournament_data["place"])
        self.tournament.players = []
        self.tournament.start_date = start_date
        self.tournament.end_date = end_date
        self.tournament.time_control = time_control
        self.tournament.description = description
        
        for player in tournament_data["players"]:
            reload_player = model_player.Player(player["name"], player["elo"], player["score"])
            self.tournament.add_player(reload_player)
            
        for round in tournament_data["rounds"]:
            reload_round = model_round.Round(round["number"])
            for match in round["matchs"]:
                player1 = model_player.Player(match["player1"]["name"], match["player1"]["elo"], match["player1"]["score"])
                player2 = model_player.Player(match["player2"]["name"], match["player1"]["elo"], match["player1"]["score"])
                
                reload_match = model_match.Match(player1, player2, match["score_player1"], match["score_player2"])   
                reload_round.add_reload_match(reload_match)

            self.tournament.add_round(reload_round)
        print(self.tournament.serializer())

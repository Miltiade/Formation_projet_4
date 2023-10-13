class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description, players, number_round=4, current_round=0):
        print("Start of Tournament initialization")  # Debugging print
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_round = number_round
        self.description = description
        self.players = players
        self.time_control = time_control
        self.current_round = current_round
        self.rounds = []
        print("End of Tournament initialization")  # Debugging print

    def add_player(self, player):
        self.players.append(player)
        
    def add_round(self, round):
        self.rounds.append(round)

# tournament1 = Tournament( # Testing: instantiating the class
#     name="Sample Tournament",
#     place="Some Place",
#     start_date="2023-10-13",
#     end_date="2023-10-14",
#     time_control="Bullet",
#     description="Sample Description"
# )
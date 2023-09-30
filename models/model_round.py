import datetime

class Round:
    def __init__(self, number, start_time= None, end_time=None):
        self.matchs = []
        self.number = number
        self.name = "Round " + str(number)
        self.start_time=start_time
        self.end_time=end_time
        
    def add_match(self, match):
        self.matchs.append(match)

    def create(self):
        # Set the start time when the round is created
        self.start_time = datetime.datetime.now()

    def mark_as_completed(self):
        # Set the end time when the round is marked as completed
        self.end_time = datetime.datetime.now()

    # def set_start_time(self, start_time):
    #     # Set the start time explicitly
    #     if start_time is None:
    #         start_time = datetime.datetime.now()
    # def set_end_time(self, end_time):
    #     # Set the end time explicitly
    #      if end_time is None:
    #         end_time = datetime.datetime.now()
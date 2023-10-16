from controlers.tournament_controler import TournamentControler
tournamentControler = TournamentControler()
tournamentControler.create_new_tournament()
print("TOURNAMENT CREATED!") # debugging print
tournamentControler.print_player()
print("PLAYERS PRINTED!") # debugging print
tournamentControler.run_first_round()
print("FIRST ROUND RUN SUCCESSFULLY!")
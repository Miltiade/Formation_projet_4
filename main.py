from controlers.tournament_controler import TournamentControler
tournamentControler = TournamentControler()
tournamentControler.create_new_tournament()
print("TOURNAMENT CREATED!")
tournamentControler.print_player() # la fonction print_player ne devrait-elle pas s'appeler print_players? Car elle print tous les players.
print("PLAYERS' LIST PRINTED!")
tournamentControler.run_first_round()
# print("FIRST ROUND RUN SUCCESSFULLY!")
tournamentControler.generate_pairs()
print("PAIRS GENERATED SUCCESSFULLY!")
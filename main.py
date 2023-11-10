# from serialization import save_tournament_state, load_tournament_state
from controlers.tournament_controler import TournamentControler

tournamentControler = TournamentControler()
# tournamentControler.create_new_tournament()
# print("TOURNAMENT CREATED!")
# tournamentControler.print_player()
# print("PLAYERS' LIST PRINTED!")
# tournamentControler.run_first_round()
# print("ROUND 1 RUN SUCCESSFULLY!")
# tournamentControler.run_subsequent_rounds()
# tournamentControler.display_final_ranking()
tournamentControler.load_tournament()
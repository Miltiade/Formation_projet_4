from controlers.tournament_controler import TournamentControler
tournamentControler = TournamentControler()
tournamentControler.create_new_tournament()
print("TOURNAMENT CREATED!")
tournamentControler.print_player() # la fonction print_player ne devrait-elle pas s'appeler print_players? Car elle print tous les players.
print("PLAYERS' LIST PRINTED!")
tournamentControler.run_first_round() # pourquoi l'utilisateur n'est-il invité à renseigner les résultats que pour 2 matches?
                                        # alors que pour les rounds suivants, c'est 4 matches?
print("FIRST ROUND RUN SUCCESSFULLY!")
tournamentControler.run_subsequent_rounds()
tournamentControler.display_final_ranking()
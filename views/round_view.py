def print_round_results(round):
    print(f"Results for Round {round.number}")
    print(f"Start Time: {round.start_time}")
    print(f"End Time: {round.end_time}")
    print("-----------------------------")
    
    for match in round.matches:
        print(f"{match.player1.name} (ELO: {match.player1.elo}) vs {match.player2.name} (ELO: {match.player2.elo})")
        print(f"Score: {match.player1.name} {match.score_player1} - {match.score_player2} {match.player2.name}")
        print("-----------------------------")
    
    print("End of Round Results")
    
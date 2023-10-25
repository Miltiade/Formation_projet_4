def enter_match_result():
    match_score = input("Which player won? Player 1 or player 2? (1 / 2 / 0) : ")
    return match_score

def print_match_result(match):
    print(f"{match.player1.name} : {match.score_player1}", f"\n{match.player2.name} : {match.score_player2}")
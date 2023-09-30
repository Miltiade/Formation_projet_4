def enter_score():
    score = input("Enter score (1 / 2 / 0) : ")
    return score

def print_match_result(match):
    print(f"{match.player1.name} : {match.score_player1}", f"\n{match.player2.name} : {match.score_player2}")
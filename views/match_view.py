def enter_match_result():
    # This function prompts the user to enter the match result.
    match_score = input(
        "Which player won? Player 1 or player 2? (Type 1 or 2. If draw, type 0) : "
    )
    return match_score


def print_match_result(match):
    # This function prints the match result.
    print(
        f"{match.player1.family_name} : {match.score_player1}\n"
        f"{match.player2.family_name} : {match.score_player2}"
    )

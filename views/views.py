##### FAIRE 1 TOURNAMENT VIEW, 1 ROUND VIEW, 1 MATCH VIEW, ET 1 PLAYER VIEW #######

def get_tournament_info():
    name = input("Enter the tournament name : ")
    time_control = input("Enter time control (Bullet/Splitz/Quick) : ")
    return name, time_control

def get_user_input(message):
    user_input = input(message)
    return user_input
    
def get_player_info():
    name = input("Enter the player name : ")
    elo = input("Enter the player elo : ")
    return name, elo
    
def print_player(players):
    for player in players:
        print(f"name : {player.name}")
        print(f"elo : {player.elo}")
        print("--------------------")
        
def enter_score():
    score = input("Enter score (1 / 2 / 0) : ")
    return score
    
def print_match_result(match):
    print(f"{match.player1.name} : {match.score_player1}", f"\n{match.player2.name} : {match.score_player2}")

def error_message(message):
    print(message)

# POSSIBLE VIEWS:
#     main_menu_view.py: Contains the Main Menu View.
#     player_management_view.py: Contains the Player Management View.
#     tournament_creation_view.py: Contains the Tournament Creation View.
#     tournament_details_view.py: Contains the Tournament Details View.
#     round_details_view.py: Contains the Round Details View.
#     match_details_view.py: Contains the Match Details View.
#     reports_view.py: Contains the Reports View.
#     save_load_view.py: Contains the Save/Load Data View.
#     error_notification_view.py: Contains the Error/Notification View.
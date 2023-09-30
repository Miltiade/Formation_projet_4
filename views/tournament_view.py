def get_tournament_info():
    name = input("Enter the tournament name : ")
    time_control = input("Enter time control (Bullet/Splitz/Quick) : ")
    return name, time_control

def get_user_input(message):
    user_input = input(message)
    return user_input

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
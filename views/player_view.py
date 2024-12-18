def get_player_info():
    name = input("Enter the player's name : ")
    elo = input("Enter the player's elo : ")
    return name, elo
    
def print_player(players):
    print("Preparing to print players. Please wait...")
    for player in players:
        print(f"family name : {player.family_name}")
        print(f"first name :  {player.first_name}")
        print(f"date of birth : {player.date_of_birth}")
        print(f"elo : {player.elo}")
        print("--------------------")
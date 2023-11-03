def get_player_info():
    name = input("Enter the player's name : ")
    elo = input("Enter the player's elo : ")
    return name, elo
    
def print_player(players):
    print("Preparing to print players. Please wait...")
    for player in players:
        print(f"name : {player.name}")
        print(f"elo : {player.elo}")
        print("--------------------")
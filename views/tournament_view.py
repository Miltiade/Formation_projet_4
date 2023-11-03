def get_tournament_info():
    name = input("Enter the tournament name : ")
    time_control = input("Enter time control (Bullet/Splitz/Quick) : ")
    return name, time_control

def get_user_input(message):
    user_input = input(message)
    return user_input

def error_message(message):
    print(message)

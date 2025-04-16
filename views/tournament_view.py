def get_tournament_info():
    # This function prompts the user to enter tournament information.
    name = input("Enter the tournament name : ")
    time_control = input("Enter time control (Bullet/Splitz/Quick) : ")
    return name, time_control

def get_user_input(message):
    # This function prompts the user for input with a custom message.
    user_input = input(message)
    return user_input

def error_message(message):
    # This function prints an error message.
    print(message)

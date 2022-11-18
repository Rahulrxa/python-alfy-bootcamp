import random


def check_input(check_type, input_parameter):
    if check_type == "RPS":
        if input_parameter == 'r' or input_parameter == 'p' or input_parameter == 's':
            return input_parameter
        else:
            return check_input("RPS", input("Invalid Input! Please enter option 'r' or 'p' or 's'"))
    if check_type == "12":
        if input_parameter == '1' or input_parameter == '2':
            return input_parameter
        else:
            return check_input("12", input("Invalid Input! Please enter option '1' or '2'"))
    if check_type == "YRN":
        if input_parameter == 'y' or input_parameter == 'n':
            return input_parameter
        else:
            return check_input("YRN", input("Invalid Input! Please enter option 'y' or 'n'"))


def versus_machine(score):
    while max(score) < 3:
        input1 = input("Enter\n'r' for Rock \n'p' for Paper \n's' for Scissors \nYour Choice:")
        input1 = check_input("RPS", input1)
        input2 = random.choice(['r', 'p', 's'])
        winner = play_game(input1, input2)
        if winner == input2:
            print("Machine choose " + input2 + ". Machine won this round")
            score[1] += 1
        elif winner == input1:
            print("User choose " + input1 + ". User won this round")
            score[0] += 1
        else:
            print("Draw")
    if score[0] > score[1]:
        print("User won this game!")
    else:
        print("Machine won this game!")


def versus_another_user(score):
    while max(score) < 3:
        input1 = input("Enter User 1 input:\n'r' for Rock \n'p' for Paper \n's' for Scissors \nYour Choice:")
        input1 = check_input("RPS", input1)
        input2 = input("Enter User 2 input:\n'r' for Rock \n'p' for Paper \n's' for Scissors \nYour Choice:")
        input2 = check_input("RPS", input2)
        winner = play_game(input1, input2)
        if winner == input2:
            print("User 2 choose " + input2 + ". User 2 won this round")
            score[1] += 1
        elif winner == input1:
            print("User 1 choose " + input1 + ". User 1 won this round")
            score[0] += 1
        elif winner == "Draw":
            print("Draw")
    if score[0] > score[1]:
        print("User won this game!")
    else:
        print("Machine won this game!")


def play_game(choice1, choice2):
    if choice1 == choice2:
        return "Draw"
    elif choice1 == 'r' and choice2 == 's':
        return choice1
    elif choice1 == 'p' and choice2 == 'r':
        return choice1
    elif choice1 == 's' and choice2 == 'p':
        return choice1
    else:
        return choice2


def start_game():
    interested = True
    score = [0, 0]
    while interested:
        input_parameter = input(
            "To start the game please select one of the options: \n Option 1:Enter '1' to play versus Machine \n Option 2: Enter '2' to play with another user\n Your Choice:")
        input_parameter = check_input("12", input_parameter)
        if input_parameter == '1':
            versus_machine(score)
        else:
            versus_another_user(score)
        another_game = input("Do you want to play another game? Press 'y' for yes and 'n' for no\n Your Choice:")
        if another_game == 'y':
            interested = True
            score = [0, 0]
        elif another_game == 'n':
            interested = False
        else:
            interested = check_input("YRN", another_game)
            score = [0, 0]


start_game()

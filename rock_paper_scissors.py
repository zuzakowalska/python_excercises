import random

moves = {1: "rock", 2: "scissors", 3: "paper"}


def game_options(options):
    print("Choose your weapon: ")
    for option in options:
        print(str(option) + ' ' + options[option])
    u = int(input("Enter number: "))
    if u not in list(options.keys()):
        print("This choice is not valid")
        game_options(options)
    else:
        print("You chose: " + options[u])
        game(options, u)


def game(options, u):
    cp = random.choice(list(options.keys()))
    print("Computer chose: " + options[cp])
    game_check = u - cp
    if game_check in [-1, 2]:
        print("You won")
    elif game_check in [-2, 1]:
        print(" You lost")
    elif game_check == 0:
        print("It's a tie")


game_options(moves)

import random

moves = {1: "rock", 2: "scissors", 3: "paper"}


def game(options, win):
    while win > -3 and win < 3:
        print("Choose your weapon: ")
        for option in options:
            print(str(option) + ' ' + options[option])
        u = int(input("Enter number: "))
        if u not in list(options.keys()):
            print("This choice is not valid")
            game(options, win)
        else:
            print("You chose: " + options[u])
            cp = random.choice(list(options.keys()))
            print("Computer chose: " + options[cp])
            game_check = u - cp
            if game_check in [-1, 2]:
                win += 1
            elif game_check in [-2, 1]:
                win -= 1
            print("Score: " + str(win))
    if win == -3:
        print("You lost")
    elif win == 3:
        print("You won")


game(moves, 0)

import random

moves = {1: "rock", 2: "scissors", 3: "paper"}
win = 0


def game_options(options, win):
    while win > -3 and win < 3:
        print("Choose your weapon: ")
        for option in options:
            print(str(option) + ' ' + options[option])
        u = int(input("Enter number: "))
        if u not in list(options.keys()):
            print("This choice is not valid")
            game_options(options, win)
        else:
            print("You chose: " + options[u])
            game(options, u, win)
    if win == -3:
        print("You lost")
    elif win == 3:
        print("You won")


def game(options, u, win):
    # cp = random.choice(list(options.keys()))
    cp = 1
    print("Computer chose: " + options[cp])
    game_check = u - cp
    if game_check in [-1, 2]:
        win += 1
    elif game_check in [-2, 1]:
        win -= 1
    game_options(options, win)

# w w w 3
# w w l 1
# w l l -1
# l l l -3


game_options(moves, win)

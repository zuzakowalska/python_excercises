import random


def guess_game():
    a = random.randint(1, 9)
    while True:
        print("Guess number between 1 and 9, type 'exit' to exit game ")
        b = input("Your guess: ")
        if b == "exit":
            return False
        else:
            if a < int(b):
                print("too high")
            elif a > int(b):
                print("too low")
            elif a == int(b):
                print("You won!")
                return False


guess_game()

import string
import random


def generate_password():
    pass_len = int(input('choose password length: '))
    while pass_len < 4:
        print('your password must be at least 4 characters long')
        pass_len = int(input('choose password length: '))
    characters = [string.ascii_letters, string.digits, string.punctuation]
    new_password = ''
    while len(new_password) < pass_len:
        new_password += random.choice(random.choice(characters))
    print(new_password)


generate_password()

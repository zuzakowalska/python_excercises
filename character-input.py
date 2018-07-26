import datetime

name = input("What's your name? ")
age = int(input ("How old are you? "))

def when_100(age):
    now = datetime.datetime.now()
    return now.year + (100 - age)

print("Your name is " + name)
print("You are " + str(age) + " years old")
print("You will be 100 in " + str(when_100(age)))


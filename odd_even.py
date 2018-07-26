num = int(input("number: "))
check = int(input("divider: "))

def odd_or_even(num, check):
    mod = num % check
    if mod == 0:
        print("number " + str(num) + " is dividable by " + str(check))
    else:
        print("number " + str(num) + " is not dividable by " + str(check))

odd_or_even(num, check)

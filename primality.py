def is_prime():
    num = int(input("Choose number: "))
    while num <= 0:
        print('not a valid number')
        num = int(input("Choose number: "))
    list_range = range(1, num+1)
    divisor_list = []
    for el in list_range:
        if num % el == 0:
            divisor_list.append(el)
    if len(divisor_list) <= 2:
        print(str(num) + ' is a prime.')
    else:
        print(divisor_list)


is_prime()

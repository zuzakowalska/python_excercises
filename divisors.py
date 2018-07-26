num = int(input("Choose number: "))

def divisor(num):
    list_range = range(1, num+1)
    divisor_list = []

    for el in list_range:
        if num % el == 0:
            divisor_list.append(el)
    print(divisor_list)

divisor(num)
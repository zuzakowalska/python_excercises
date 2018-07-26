num = int(input("number: "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than_5(list, num):
    b = []
    for el in list:
        if el < num:
            b.append(el)
    print(b)

less_than_5(a, num)
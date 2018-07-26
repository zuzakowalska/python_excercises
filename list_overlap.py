import random

number = int(input("How many lists: "))

def new_list():
    single_list = []
    count = random.sample(range(1,11), 1)
    single_list.extend(random.sample(range(10), count[0]))
    return single_list

def lists_generator(number):
    lists = [new_list() for i in range(number)]
    def overlap(lists):
        for i in range(0, len(lists)):
            if i+1 not in range(0, len(lists)):
                break
            else:
                overlapped = set(lists[i]) & set(lists[i+1])
        print(lists, overlapped)

    overlap(lists)

lists_generator(number)

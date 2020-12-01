dict_of_remainders = dict()
value_to_target = 2020

with open("expenses.txt") as expenses:
    expenses = list(map(int, expenses.readlines()))

    for number in expenses:
        dict_of_remainders[value_to_target - number] = number

    for key, value in dict_of_remainders.items():
        set_of_remainders = set()
        for number in expenses:
            if number in set_of_remainders:
                print(number * value * (key - number))
            set_of_remainders.add(key - number)

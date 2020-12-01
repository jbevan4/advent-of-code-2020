set_of_remainder_expenses = set()
value_to_target = 2020

with open("expenses.txt") as expenses:
    for line in expenses.readlines():
        number = int(line)
        if number in set_of_remainder_expenses:
            print(number * (value_to_target - number))
        set_of_remainder_expenses.add(value_to_target - number)

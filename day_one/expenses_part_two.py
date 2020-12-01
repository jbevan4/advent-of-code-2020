from expenses_part_one import find_two_expenses_that_sum_to_value


def find_three_expenses_that_sum_to_value(target, expenses):
    dict_of_remainders = dict()
    for number in expenses:
        dict_of_remainders[target - number] = number

    for key, value in dict_of_remainders.items():
        set_of_remainders = set()
        pair = find_two_expenses_that_sum_to_value(
            target=key, expenses=expenses)
        if pair:
            return value * pair[0] * pair[1]
        set_of_remainders.add(key - number)


with open("expenses.txt") as expenses:
    expenses = list(map(int, expenses.readlines()))
    print(find_three_expenses_that_sum_to_value(target=2020, expenses=expenses))

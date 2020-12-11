def find_two_expenses_that_sum_to_value(target, expenses):
    set_of_remainder_expenses = set()
    for expense in expenses:
        if expense in set_of_remainder_expenses:
            return (expense, (target - expense))
        set_of_remainder_expenses.add(target - expense)
    return None


if __name__ == "__main__":
    with open("expenses.txt") as expenses:
        pair = find_two_expenses_that_sum_to_value(
            target=2020, expenses=map(int, expenses.readlines()))
        if pair is not None:
            print(pair[0] * pair[1])

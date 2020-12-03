from collections import Counter


def sanitize_passwords(passwords):
    return passwords.strip()


def sanitize_validation(validators):
    """sanitize validation in the form xn-yn z"""
    joined_bounds, letter = validators.split()
    lower_bound, upper_bound = map(int, joined_bounds.split("-"))
    return lower_bound, upper_bound, letter


if __name__ == "__main__":
    with open("passwords.txt") as passwords:
        valid_passwords = 0
        for line in passwords.readlines():
            validation_rules, password_to_check = line.strip().split(":")
            lower_bound, upper_bound, letter = sanitize_validation(
                validation_rules)
            password = sanitize_passwords(password_to_check)
            letter_counter = Counter(password)
            if lower_bound <= letter_counter.get(letter, 0) <= upper_bound:
                valid_passwords += 1
        print(valid_passwords)

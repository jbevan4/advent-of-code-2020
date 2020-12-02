def sanitize_passwords(passwords):
    return passwords.strip()


def sanitize_validation(validators):
    """sanitize validation in the form xn-yn z"""
    joined_bounds, letter = validators.split()
    first_position, second_position = map(int, joined_bounds.split("-"))
    return first_position - 1, second_position - 1, letter


with open("passwords.txt") as passwords:
    valid_passwords = 0
    for line in passwords.readlines():
        validation_rules, password_to_check = line.strip().split(":")
        first_position, second_position, letter = sanitize_validation(
            validation_rules)
        password = sanitize_passwords(password_to_check)
        if bool(password[first_position] == letter) ^ bool(password[second_position] == letter):
            valid_passwords += 1
    print(valid_passwords)

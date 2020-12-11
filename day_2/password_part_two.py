from password_part_one import sanitize_passwords, sanitize_validation


if __name__ == "__main__":
    with open("passwords.txt") as passwords:
        valid_passwords = 0
        for line in passwords.readlines():
            validation_rules, password_to_check = line.strip().split(":")
            first_position, second_position, letter = sanitize_validation(
                validation_rules)
            password = sanitize_passwords(password_to_check)
            if bool(password[first_position - 1] == letter) ^ bool(password[second_position - 1] == letter):
                valid_passwords += 1
        print(valid_passwords)

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def ingest_file():
    with open("passports.txt") as passports:
        return [line.strip() for line in passports.readlines()]


def generate_passport_keys(raw_data):
    passport_keys = list()
    current_passport = ""
    for line in raw_data:
        current_passport += " " + line
        if line == "":
            passport_keys.append(current_passport)
            current_passport = ""
    # ingest last line
    passport_keys.append(current_passport)
    return passport_keys


def is_passport_valid(pp):
    for field in fields:
        if field not in pp:
            return False
    return True


if __name__ == "__main__":
    data = ingest_file()
    passport_keys = generate_passport_keys(data)
    print(sum(1 for key in passport_keys if is_passport_valid(key)))

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def ingest_file():
    with open("passports.txt") as passports:
        return [line.strip() for line in passports.read().split("\n\n")]


def is_passport_valid(pp):
    for field in fields:
        if field not in pp:
            return False
    return True


if __name__ == "__main__":
    data = ingest_file()
    print(sum(1 for passport in data if is_passport_valid(passport)))

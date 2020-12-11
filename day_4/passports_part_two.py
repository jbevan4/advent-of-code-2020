from passports_part_one import fields, ingest_file, generate_passport_keys, is_passport_valid
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
good_passports = []


def is_valid_pid(pid):
    return False if len(pid) != 9 else True


def is_valid_ecl(ecl):
    if ecl in "amb blu brn gry grn hzl oth":
        return True
    return False


def is_valid_hcl(hcl):
    if hcl[0] != "#":
        return False
    if len(hcl[1:]) != 6:
        return False
    return True


def is_valid_hgt(hgt):
    units = hgt[-2:]
    if units not in ["cm", "in"]:
        return False
    height = int(hgt[:-2])
    if units == "cm":
        return 150 <= height <= 193
    if units == "in":
        return 59 <= height <= 76
    return False


def is_valid_eyr(eyr):
    eyr = int(eyr)
    return 2020 <= eyr <= 2030


def is_valid_iyr(iyr):
    iyr = int(iyr)
    return 2010 <= iyr <= 2020


def is_valid_byr(byr):
    byr = int(byr)
    return 1920 <= byr <= 2002


def is_valid_data(passport):
    passport = passport.split()
    dict_of_values = {}
    for fields in passport:
        key, value = fields.split(":")
        dict_of_values[key] = value

    if not is_valid_byr(dict_of_values["byr"]):
        return False

    if not is_valid_iyr(dict_of_values["iyr"]):
        return False

    if not is_valid_eyr(dict_of_values["eyr"]):
        return False

    if not is_valid_hgt(dict_of_values["hgt"]):
        return False

    if not is_valid_hcl(dict_of_values["hcl"]):
        return False

    if not is_valid_ecl(dict_of_values["ecl"]):
        return False

    if not is_valid_pid(dict_of_values["pid"]):
        return False

    return True


if __name__ == "__main__":
    data = ingest_file()
    passport_keys = generate_passport_keys(data)
    good_passports = [
        passport for passport in passport_keys if is_passport_valid(passport)]
    count = 0
    for pp in good_passports:
        if is_valid_data(pp):
            count += 1
    print(count)

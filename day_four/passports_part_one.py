fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def is_passport_valid(pp):
    for field in fields:
        if field not in pp:
            return False
    return True


with open("passports.txt") as passports:
    data = passports.readlines()
    data = [line.strip() for line in data]

valid_count = 0
current_passport = ""
for line in data:
    if line != '':
        current_passport += ' ' + line
    else:
        print(current_passport)
        if is_passport_valid(current_passport):
            valid_count += 1
        current_passport = ""
if is_passport_valid(current_passport):
    valid_count += 1
print(valid_count)

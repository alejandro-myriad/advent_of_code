# Part 1: How many valid passports (has all required fields)
import re

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
optional_fields = {"cid"}


def check_entry(entry):
    fields = {key_value_pair.split(":")[0] for key_value_pair in entry}
    return not (required_fields - fields)


with open("input") as f:
    entries = [re.split(r"\s+", group) for group in f.read().strip().split("\n\n")]
    valid_count = 0
    for entry in entries:
        if check_entry(entry):
            valid_count += 1
print(valid_count)

# Part 2: How many valid passports (has all required fields)
import re

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
optional_fields = {"cid"}


def check_entry(entry):
    passport = dict([key_value_pair.split(":") for key_value_pair in entry])
    if required_fields - set(passport):
        return False
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False
    if passport["hgt"].endswith("cm"):
        if int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193:
            return False
    elif passport["hgt"].endswith("in"):
        if int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
            return False
    else:
        return False
    if not re.match(r"^#[a-z0-9]{6}$", passport["hcl"]):
        return False
    if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    if not re.match(r"^\d{9}$", passport["pid"]):
        return False

    return True


with open("input") as f:
    entries = [re.split(r"\s+", group) for group in f.read().strip().split("\n\n")]
    valid_count = 0
    for entry in entries:
        if check_entry(entry):
            valid_count += 1
print(valid_count)

# Part 1: min/max letter count
import re
def check_password(password_entry):
    m = re.match(r"(\d+)-(\d+) ([a-z]): (\w+)", password_entry)
    minimum, maximum, letter, password = m.groups()
    letter_count = password.count(letter)
    return letter_count >= int(minimum) and letter_count <= int(maximum)

with open("input") as f:
    valid_count = 0
    for password_entry in f.readlines():
        if check_password(password_entry.strip()):
            valid_count += 1
    print(valid_count)

# Part 2: exactly one instance of letter at position
import re
def check_password(password_entry):
    m = re.match(r"(\d+)-(\d+) ([a-z]): (\w+)", password_entry)
    pos1, pos2, letter, password = m.groups()
    return (password[int(pos1) - 1] == letter) ^ (password[int(pos2) - 1] == letter)

with open("input") as f:
    valid_count = 0
    for password_entry in f.readlines():
        if check_password(password_entry.strip()):
            valid_count += 1
    print(valid_count)

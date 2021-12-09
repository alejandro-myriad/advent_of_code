# public_key_door = 17807724
# public_key_card = 5764801

public_key_door = 6270530
public_key_card = 14540258

DIVISOR = 20201227

def transform_step(value, subject_matter):
    value *= subject_matter
    value %= DIVISOR
    return value

def transform(subject_matter, loop_size):
    value = 1
    for _ in range(loop_size):
        value = transform_step(value, subject_matter)
    return value

def get_loop_size(public_key):
    value = 1
    subject_matter = 7
    loop_size = 0
    while value != public_key:
        value = transform_step(value, subject_matter)
        loop_size += 1
    return loop_size

loop_size_door = get_loop_size(public_key_door)
loop_size_card = get_loop_size(public_key_card)

encryption_key_1 = transform(public_key_door, loop_size_card)
encryption_key_2 = transform(public_key_card, loop_size_door)

print(encryption_key_1)
print(encryption_key_2)

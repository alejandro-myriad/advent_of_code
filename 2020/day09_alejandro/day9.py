def has_pair(previous_numbers, number):
    if len(previous_numbers) < 2:
        return False

    for n in previous_numbers[1:]:
        if previous_numbers[0] + n == number:
            return True
    return has_pair(previous_numbers[1:], number)


def find_bad_number(numbers, preamble_length):
    assert len(numbers) > preamble_length

    previous_numbers = numbers[:preamble_length]
    number = numbers[preamble_length]
    if not has_pair(previous_numbers, number):
        return number
    return find_bad_number(numbers[1:], preamble_length)


def find_encryption_weakness(numbers, bad_number):
    contiguous_range = []
    range_sum = 0
    for number in numbers:
        contiguous_range.append(number)
        range_sum += number
        if range_sum == bad_number:
            return contiguous_range
        elif range_sum > bad_number:
            return find_encryption_weakness(numbers[1:], bad_number)
    assert False

def main():
    PREAMBLE_LENGTH = 25
    with open("input") as f:
        numbers = [int(entry) for entry in f.read().strip().split("\n")]

    bad_number = find_bad_number(numbers, PREAMBLE_LENGTH)
    print(bad_number)
    weakness = find_encryption_weakness(numbers, bad_number)
    print((weakness, sum(weakness)))
    print(min(weakness) + max(weakness))


if __name__ == "__main__":
    main()


from collections import defaultdict

test_input = "0,3,6"
real_input = "0,20,7,16,1,18,15"

numbers = list(map(int, real_input.split(",")))
index = 1
numbers_index = defaultdict(list)
for number in numbers:
    numbers_index[number] = [index]
    index += 1
    last_number = number



for _ in range(30000000 - len(numbers)):
    if len(numbers_index[last_number]) == 1:
        last_number = 0
    else:
        last_number = index - numbers_index[last_number][-2] - 1

    numbers_index[last_number].append(index)
    index += 1

print(last_number)

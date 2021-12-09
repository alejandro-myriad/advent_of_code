# Part 1: product of 2 numbers that sum to 2020
with open("input") as f:
    nums = set(f.read().split("\n"))

nums.remove("")
for num in nums:
    num = int(num)
    if str(2020 - num) in nums:
        print(f"{num} * {2020 - num} = {num * (2020 - num)}")

# Part 2: product 3 numbers that sum to 2020
with open("input") as f:
    nums = set(f.read().split("\n"))

nums.remove("")
for num1 in nums:
    num1 = int(num1)
    remainder = 2020 - num1
    for num2 in (nums - {num1}):
        num2 = int(num2)
        num3 = 2020 - num1 - num2
        if str(num3) in nums:
            print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3}")

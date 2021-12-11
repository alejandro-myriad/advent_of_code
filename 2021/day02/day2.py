
def main():
    with open("input") as f:
        instructions = [entry.split(" ") for entry in f.read().strip().split("\n")]

    hor = depth = aim = 0
    for direction, num in instructions:
        num = int(num)
        if direction == "forward":
            hor += num
            depth += num * aim
        elif direction == "down":
            aim += num
        elif direction == "up":
            aim -= num
    print(hor * depth)



if __name__ == "__main__":
    main()


def main():
    with open("input") as f:
        measurements = [int(entry) for entry in f.read().strip().split("\n")]

    sums = [sum(measurements[i:i+3]) for i in range(len(measurements) - 2)]
    print(sums)


    prev_sum = sums[0]
    count = 0
    for s in sums[1:]:
        if s > prev_sum:
            count += 1
        prev_sum = s

    print(count)


if __name__ == "__main__":
    main()

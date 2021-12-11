
def main():
    with open("input") as f:
        numbers = [entry for entry in f.read().strip().split("\n")]

    gamma_rate = epsilon_rate = ""
    from collections import defaultdict
    bit_counts = defaultdict(list)
    for number in numbers:
        for i, bit in enumerate(number):
            bit_counts[i].append(bit)

    for position, bits in sorted(bit_counts.items()):
        if bits.count("1") > bits.count("0"):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    print("gamma * epsilon =", int(gamma_rate, 2) * int(epsilon_rate, 2))


    import copy
    oxygen = copy.copy(numbers)
    for i in range(len(oxygen[0])):
        if len(oxygen) == 1:
            break
        bits = [number[i] for number in oxygen]
        num_ones = bits.count("1")
        num_zeroes = bits.count("0")

        if num_ones >= num_zeroes:
            oxygen = [number for number in oxygen if number[i] == "1"]
        else:
            oxygen = [number for number in oxygen if number[i] == "0"]

    [oxygen] = oxygen

    co2 = copy.copy(numbers)
    for i in range(len(co2[0])):
        if len(co2) == 1:
            break
        bits = [number[i] for number in co2]
        num_ones = bits.count("1")
        num_zeroes = bits.count("0")


        if num_zeroes <= num_ones:
            co2 = [number for number in co2 if number[i] == "0"]
        else:
            co2 = [number for number in co2 if number[i] == "1"]

    [co2] = co2
    print("oxygen * co2 = ", int(co2,2) * int(oxygen,2))




if __name__ == "__main__":
    main()

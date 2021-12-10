def main():
    with open("input") as f:
        entries = [position for position in f.read().strip().split("\n")]
    entries = [entry.split(" | ") for entry in entries]
    output_numbers = []
    for patterns, outputs in entries:
        patterns = list(map(lambda v: "".join(sorted(v)), patterns.split(" ")))
        outputs = list(map(lambda v: "".join(sorted(v)), outputs.split(" ")))
        value2number = {}
        number2value = {}
        for value in patterns + outputs:
            if len(value) == 2:
                value2number[value] = "1"
                number2value["1"] = value
            elif len(value) == 3:
                value2number[value] = "7"
                number2value["7"] = value
            elif len(value) == 4:
                value2number[value] = "4"
                number2value["4"] = value
            elif len(value) == 7:
                value2number[value] = "8"
                number2value["8"] = value
        for value in patterns + outputs:
            if len(value) == 5:
                if set(number2value["7"]).issubset(set(value)):
                    value2number[value] = "3"
                    number2value["3"] = value
                elif len(set(number2value["4"]).intersection(set(value))) == 3:
                    value2number[value] = "5"
                    number2value["5"] = value
                else:
                    value2number[value] = "2"
                    number2value["2"] = value
            elif len(value) == 6:
                if set(number2value["4"]).issubset(set(value)):
                    value2number[value] = "9"
                    number2value["9"] = value
                elif len(set(number2value["1"]).intersection(set(value))) == 1:
                    value2number[value] = "6"
                    number2value["6"] = value
                else:
                    value2number[value] = "0"
                    number2value["0"] = value
        output_numbers.append(int("".join(map(lambda v: value2number[v], outputs))))

    print(sum(output_numbers))

if __name__ == "__main__":
    main()

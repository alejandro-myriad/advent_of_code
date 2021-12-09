import re


def calc_value_with_mask(value, mask):
    assert mask, "mask was empty"
    b_value = bin(int(value))[2:]
    b_value = ("0" * (len(mask) - len(b_value))) + b_value
    b_value_reversed = list(reversed(b_value))
    mask_reversed = list(reversed(mask))
    new_value_reversed = []
    for bit, masked_bit in zip(b_value_reversed, mask_reversed):
        new_value_reversed.append(bit if masked_bit == "X" else masked_bit)
    return int("".join(reversed(new_value_reversed)), 2)


def part1():
    with open("input") as f:
        instructions = f.read().strip().split("\n")
    mask_r = re.compile(r"mask = (.*)")
    mem_r = re.compile(r"mem\[(\d*)\] = (.*)")
    mask = None
    mem = {}
    for instruction in instructions:
        mask_match = mask_r.match(instruction)
        mem_match = mem_r.match(instruction)
        if mask_match:
            mask = mask_match.group(1)
        elif mem_match:
            mem[mem_match.group(1)] = calc_value_with_mask(mem_match.group(2), mask)
        else:
            assert False, f"got unexpected instruction {instruction}"
    print(mem)
    print(sum(mem.values()))


def apply_address_mask(address, mask):
    assert mask, "mask was empty"
    b_address = bin(int(address))[2:]
    b_address = ("0" * (len(mask) - len(b_address))) + b_address
    b_address_reversed = list(reversed(b_address))
    mask_reversed = list(reversed(mask))
    new_address_reversed = []
    for bit, masked_bit in zip(b_address_reversed, mask_reversed):
        new_address_reversed.append(bit if masked_bit == "0" else masked_bit)
    return "".join(reversed(new_address_reversed))


def calc_floating_addresses(addresses):
    new_addresses = []
    done = True
    for address in addresses:
        if "X" in address:
            done = False
            new_addresses.append(address.replace("X", "1", 1))
            new_addresses.append(address.replace("X", "0", 1))
        else:
            new_addresses.append(address)

    if done:
        return new_addresses

    return calc_floating_addresses(new_addresses)


def part2():
    with open("input") as f:
        instructions = f.read().strip().split("\n")
    mask_r = re.compile(r"mask = (.*)")
    mem_r = re.compile(r"mem\[(\d*)\] = (.*)")
    mask = None
    mem = {}
    for instruction in instructions:
        mask_match = mask_r.match(instruction)
        mem_match = mem_r.match(instruction)
        if mask_match:
            mask = mask_match.group(1)
        elif mem_match:
            address = apply_address_mask(mem_match.group(1), mask)
            addresses = calc_floating_addresses([address])
            for address in addresses:
                mem[address] = int(mem_match.group(2))
        else:
            assert False, f"got unexpected instruction {instruction}"
    print(mem)
    print(sum(mem.values()))


def main():
    part2()


if __name__ == "__main__":
    main()

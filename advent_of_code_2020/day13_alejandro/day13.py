import math

# Part 1: adjacent seats


def part1():
    with open("input") as f:
        i = f.read().strip().split("\n")
        ready_to_depart_time = int(i[0])
        bus_ids = [
            (int(bus_id) if bus_id.isdigit() else bus_id) for bus_id in i[1].strip().split(",")
        ]
    next_departures = [
        (bus_id * (ready_to_depart_time // bus_id + 1), bus_id)
        for bus_id in bus_ids
        if bus_id != "x"
    ]
    wait_times = [
        (next_depart_time - ready_to_depart_time, bus_id)
        for next_depart_time, bus_id in next_departures
    ]
    bus_ids_indexed = [(bus_id, index) for index, bus_id in enumerate(bus_ids) if bus_id != "x"]

    def check_bus_ids(multiple):
        time = bus_ids[0] * multiple
        return all([(time + index) % bus_id == 0 for bus_id, index in bus_ids_indexed[1:]])

    multiple = 0
    while not check_bus_ids(multiple):
        multiple += 1

    print(bus_ids_indexed)
    print(multiple)
    print(multiple * bus_ids_indexed[0][0])


def gcd(num1, num2):
    b, a = sorted((num1, num2))
    print((a, b))
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


def part2():
    with open("test_input") as f:
        i = f.read().strip().split("\n")
        bus_ids = i[1].strip().split(",")

        bus_ids_with_offsets = []
        for offset, bus_id in enumerate(bus_ids):
            if bus_id.isdigit():
                bus_ids_with_offsets.append((int(bus_id), offset))
    print(bus_ids)
    print(bus_ids_with_offsets)
    print("\n".join(f"x = {offset} (mod {bus_id})" for bus_id, offset in bus_ids_with_offsets))
    total_bus_ids = sum(t[0] for t in bus_ids_with_offsets)
    total_offsets = sum(t[1] for t in bus_ids_with_offsets)
    print(total_bus_ids)
    print(total_offsets)

def check_route(timestamp, bus_ids_with_offsets):
    for bus_id, offset in bus_ids_with_offsets)


if __name__ == "__main__":
    part2()

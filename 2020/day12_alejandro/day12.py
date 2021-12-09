import math

# Part 1: adjacent seats
def part1():
    with open("input") as f:
        instructions = f.read().strip().split("\n")
    pos = [0, 0]
    direction_vector = [1, 0]
    for instruction in instructions:
        action = instruction[0]
        number = int(instruction[1:])
        if action == "F":
            pos[0] += number * direction_vector[0]
            pos[1] += number * direction_vector[1]
        elif action == "L":
            dv = list(direction_vector)
            direction_vector[0] = (
                round(math.cos(math.radians(number)) * dv[0])
                - round(math.sin(math.radians(number)) * dv[1])
            )
            direction_vector[1] = (
                round(math.sin(math.radians(number)) * dv[0])
                + round(math.cos(math.radians(number)) * dv[1])
            )
        elif action == "R":
            dv = list(direction_vector)
            direction_vector[0] = (
                round(math.cos(math.radians(-1 * number)) * dv[0])
                - round(math.sin(math.radians(-1 * number)) * dv[1])
            )
            direction_vector[1] = (
                round(math.sin(math.radians(-1 * number)) * dv[0])
                + round(math.cos(math.radians(-1 * number)) * dv[1])
            )
        elif action == "N":
            pos[1] += number
        elif action == "E":
            pos[0] += number
        elif action == "W":
            pos[0] -= number
        elif action == "S":
            pos[1] -= number
        else:
            assert False

        print((instruction, pos, direction_vector))
    print(abs(pos[1]) + abs(pos[0]))

# Part 2: visible seats
def part2():
    with open("input") as f:
        instructions = f.read().strip().split("\n")
    pos = [0, 0]
    waypoint = [10, 1]
    for instruction in instructions:
        action = instruction[0]
        number = int(instruction[1:])
        if action == "F":
            pos[0] += number * waypoint[0]
            pos[1] += number * waypoint[1]
        elif action == "L":
            wp = list(waypoint)
            waypoint[0] = (
                round(math.cos(math.radians(number))) * wp[0]
                - round(math.sin(math.radians(number))) * wp[1]
            )
            waypoint[1] = (
                round(math.sin(math.radians(number))) * wp[0]
                + round(math.cos(math.radians(number))) * wp[1]
            )
        elif action == "R":
            wp = list(waypoint)
            waypoint[0] = (
                round(math.cos(math.radians(-1 * number))) * wp[0]
                - round(math.sin(math.radians(-1 * number))) * wp[1]
            )
            waypoint[1] = (
                round(math.sin(math.radians(-1 * number))) * wp[0]
                + round(math.cos(math.radians(-1 * number))) * wp[1]
            )
        elif action == "N":
            waypoint[1] += number
        elif action == "E":
            waypoint[0] += number
        elif action == "W":
            waypoint[0] -= number
        elif action == "S":
            waypoint[1] -= number
        else:
            assert False

        print((instruction, pos, waypoint))
    print(abs(pos[1]) + abs(pos[0]))

if __name__ == "__main__":
    part2()

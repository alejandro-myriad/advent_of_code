from collections import defaultdict
from copy import deepcopy


# Part 1: adjacent seats
def part1():
    with open("input") as f:
        seats = [list(row.strip()) for row in f.read().strip().split("\n")]

    print("\n".join(map("".join, seats)))

    def iterate(seats):
        new_seats = deepcopy(seats)
        for row_i in range(len(seats)):
            for col_i in range(len(seats[0])):
                seat = seats[row_i][col_i]
                adjacent_seats = []
                if row_i > 0 and col_i > 0:
                    adjacent_seats.append(seats[row_i - 1][col_i - 1])
                if row_i > 0:
                    adjacent_seats.append(seats[row_i - 1][col_i])
                if row_i > 0 and col_i < len(seats[0]) - 1:
                    adjacent_seats.append(seats[row_i - 1][col_i + 1])
                if col_i > 0:
                    adjacent_seats.append(seats[row_i][col_i - 1])
                if col_i < len(seats[0]) - 1:
                    adjacent_seats.append(seats[row_i][col_i + 1])
                if col_i > 0 and row_i < len(seats) - 1:
                    adjacent_seats.append(seats[row_i + 1][col_i - 1])
                if row_i < len(seats) - 1:
                    adjacent_seats.append(seats[row_i + 1][col_i])
                if row_i < len(seats) - 1 and col_i < len(seats[0]) - 1:
                    adjacent_seats.append(seats[row_i + 1][col_i + 1])

                if seat == "#" and adjacent_seats.count("#") >= 4:
                    new_seats[row_i][col_i] = "L"
                elif seat == "L" and adjacent_seats.count("#") == 0:
                    new_seats[row_i][col_i] = "#"
        return new_seats

    prev_seats = None
    while seats != prev_seats:
        prev_seats = seats
        seats = iterate(prev_seats)

    seats = [seat for row in seats for seat in row]
    print(seats.count("#"))


def find_visible(seats, row_i, col_i, row_delta, col_delta):
    visible_seat = "."
    while visible_seat == ".":
        row_i += row_delta
        col_i += col_delta
        if row_i < 0 or col_i < 0 or row_i >= len(seats) or col_i >= len(seats[0]):
            visible_seat = None
        else:
            visible_seat = seats[row_i][col_i]
    return visible_seat

def iterate(seats):
    new_seats = deepcopy(seats)
    for row_i in range(len(seats)):
        for col_i in range(len(seats[0])):
            seat = seats[row_i][col_i]
            if seat != ".":
                visible_seats = []
                visible_seats.append(find_visible(seats, row_i, col_i, -1, -1))
                visible_seats.append(find_visible(seats, row_i, col_i, 0, -1))
                visible_seats.append(find_visible(seats, row_i, col_i, 1, -1))
                visible_seats.append(find_visible(seats, row_i, col_i, -1, 0))
                visible_seats.append(find_visible(seats, row_i, col_i, 1, 0))
                visible_seats.append(find_visible(seats, row_i, col_i, -1, 1))
                visible_seats.append(find_visible(seats, row_i, col_i, 0, 1))
                visible_seats.append(find_visible(seats, row_i, col_i, 1, 1))
                if seat == "#" and visible_seats.count("#") >= 5:
                    new_seats[row_i][col_i] = "L"
                elif seat == "L" and visible_seats.count("#") == 0:
                    new_seats[row_i][col_i] = "#"
    return new_seats


def part2():
    with open("input") as f:
        seats = [list(row.strip()) for row in f.read().strip().split("\n")]

    prev_seats = None
    while seats != prev_seats:
        prev_seats = seats
        seats = iterate(prev_seats)

    flat_seats = [seat for row in seats for seat in row]
    print(flat_seats.count("#"))

if __name__ == "__main__":
    part2()

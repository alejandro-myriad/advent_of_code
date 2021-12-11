import re
import numpy as np

def parse_line(line):
    points = re.match(r"^(\d+),(\d+) -> (\d+),(\d+)$", line).groups()
    points = list(map(int, points))
    x1, y1, x2, y2 = points
    return (x1, y1), (x2, y2)


def main():
    with open("input") as f:
        lines = [line for line in f.read().strip().split("\n")]
    lines = list(map(parse_line, lines))

    max_x = max_y = 0
    for ((x1, y1), (x2, y2)) in lines:
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2

    print(max_x, max_y)
    grid = np.zeros((max_x + 1, max_y + 1))

    for ((x1, y1), (x2, y2)) in lines:
        identity = np.identity(min(abs(x1 - x2), abs(y1 - y2))+ 1)
        if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            identity = np.fliplr(identity)
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        grid[y1:y2 + 1,x1:x2 + 1] += identity

    print(np.shape(np.where(grid > 1))[1])




if __name__ == "__main__":
    main()

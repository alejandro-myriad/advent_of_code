import re
def fold_vertical(points, val):
    new_points = set()
    for point in points:
        x, y = point
        if x > val:
            x -= 2 * (x - val)
        new_points.add((x, y))
    return new_points

def fold_horizontal(points, val):
    new_points = set()
    for point in points:
        x, y = point
        if y > val:
            y -= 2 * (y - val)
        new_points.add((x, y))
    return new_points

def fold_paper(points, fold):
    var, val = fold
    if var == 'x':
        return fold_vertical(points, val)
    elif var == 'y':
        return fold_horizontal(points, val)
    else:
        assert False

import numpy as np
def main():
    with open("input") as f:
        points, folds = [group.split("\n") for group in f.read().strip().split("\n\n")]

    points = {tuple(map(int, p.split(","))) for p in points}
    c = re.compile(r"^fold along ([xy])=(\d+)$")
    folds = [c.match(f).groups() for f in folds]
    folds = [(var, int(val)) for var, val in folds]
    for fold in folds:
        points = fold_paper(points, fold)
        print(len(points))
    max_x = sorted(points)[-1][0]
    max_y = sorted(points, key=lambda t: t[1])[-1][1]
    print(max_x, max_y)

    grid = np.zeros((max_y + 1, max_x+1))
    for point in points:
        x, y = point
        grid[(y, x)] = 1
    for row in grid:
        print("".join(["." if v == 0 else "#" for v in row]))


if __name__ == "__main__":
    main()

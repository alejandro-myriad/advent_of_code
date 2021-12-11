import sys
import re
import numpy as np


def flash(grid):
    grid += 1
    max_y, max_x = grid.shape
    while np.where(grid == 10)[0].size > 0:
        flash_points = set(zip(*np.where(grid == 10)))
        while flash_points:
            y, x  = flash_points.pop()
            grid[max(0, y-1):min(y+2, max_y),max(0, x-1):min(x+2, max_x)] += 1
            flash_points.update(zip(*np.where(grid == 10)))
    grid *= grid < 10

def main():
    with open("input") as f:
        grid = np.array([list(map(int, row)) for row in f.read().strip().split("\n")])

    flash_count = 0
    iteration = 0
    max_y, max_x = grid.shape
    while(flash_count < (max_y * max_x)):
        iteration += 1
        flash(grid)
        flash_count = np.where(grid == 0)[0].size
        print(iteration, flash_count)


if __name__ == "__main__":
    main()

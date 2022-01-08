import numpy as np
import math
from heapq import heappush, heappop


def get_neighbors(current_pos, shape):
    y, x = current_pos
    max_y, max_x = shape
    neighbors = []
    if x > 0:
        neighbors.append((y, x - 1))
    if x < max_x - 1:
        neighbors.append((y, x + 1))
    if y > 0:
        neighbors.append((y - 1, x))
    if y < max_y - 1:
        neighbors.append((y + 1, x))
    return neighbors


def main():
    with open("input") as f:
        original_grid = np.array([list(map(int, row)) for row in f.read().strip().split("\n")])

    # create expanded grid
    height, width = original_grid.shape
    grid = np.zeros((height * 5, width * 5))
    for i in range(5):
        for j in range(5):
            adder = np.vectorize(lambda v: v + i + j if v + i + j <= 9 else ((v + i + j) % 9))
            tile = grid[i*height:(i+1)*height, j*width:(j+1)*width] 
            grid[i*height:(i+1)*height, j*width:(j+1)*width] = adder(original_grid)


    max_y, max_x = grid.shape
    current = (0, 0)
    total_risk = np.ones_like(grid) * math.inf
    total_risk[current] = 0
    nodes_to_visit = [(total_risk[(0,0)], (0,0))]
    visited = set()
    while nodes_to_visit:
        current_risk, current_pos = heappop(nodes_to_visit)
        if current_pos in visited:
            continue
        if current_pos == (max_y - 1, max_x - 1):
            print(current_risk)
            return
        visited.add(current_pos)
        y, x = current_pos
        for neighbor in get_neighbors(current_pos, grid.shape):
            if neighbor not in visited:
                total_risk[neighbor] = min(
                    total_risk[neighbor],
                    total_risk[current_pos] + grid[neighbor],
                )
                heappush(nodes_to_visit, (total_risk[neighbor], neighbor))



if __name__ == "__main__":
    main()

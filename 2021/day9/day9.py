import numpy as np
def _get_basin_points(heightmap, max_x, max_y, point, basin_points):
    y, x = point
    if point in basin_points:
        return
    if y < 0 or y >= max_y or x < 0 or x >= max_x or heightmap[point] == 9:
        return
    basin_points.add(point)
    _get_basin_points(heightmap, max_x, max_y, (y + 1, x), basin_points)
    _get_basin_points(heightmap, max_x, max_y, (y - 1, x), basin_points)
    _get_basin_points(heightmap, max_x, max_y, (y, x - 1), basin_points)
    _get_basin_points(heightmap, max_x, max_y, (y, x + 1), basin_points)


def get_basin_size(heightmap, lowpoint):
    max_y, max_x = heightmap.shape
    basin_points = set()
    _get_basin_points(heightmap, max_x, max_y, lowpoint, basin_points)
    return len(basin_points)


def main():
    with open("input") as f:
        heightmap = np.array([list(map(int, row)) for row in f.read().strip().split("\n")])

    print(heightmap.shape)
    max_y, max_x = heightmap.shape
    lowpoints = []
    for iy, ix in np.ndindex(heightmap.shape):
        height = heightmap[iy, ix]
        if iy > 0 and heightmap[iy - 1, ix] <= height:
            continue
        if iy < max_y - 1 and heightmap[iy + 1, ix] <= height:
            continue
        if ix > 0 and heightmap[iy, ix - 1] <= height:
            continue
        if ix < max_x - 1 and heightmap[iy, ix + 1] <= height:
            continue
        # lowpoints.append(height)
        lowpoints.append((iy, ix))
    # print(sum(lowpoints) + len(lowpoints))
    print(lowpoints)
    basin_sizes = []
    for point in lowpoints:
        basin_sizes.append(get_basin_size(heightmap, point))
    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

        


if __name__ == "__main__":
    main()

def parse_tiles(tiles):
    c = regex.compile(r"^(e|se|sw|w|nw|ne)*$")
    return c.match(tiles).captures(1)


with open("input") as f:
    tiles_to_flip = list(map(parse_tiles, f.read().strip().split("\n")))


def calc_pos(tile):
    pos = [0, 0]
    for direction in tile:
        if direction == "e":
            pos[0] += 1
            pos[1] += 0
        elif direction == "se":
            pos[0] += 1
            pos[1] += 1
        elif direction == "sw":
            pos[0] += 0
            pos[1] += 1
        elif direction == "w":
            pos[0] += -1
            pos[1] += 0
        elif direction == "nw":
            pos[0] += -1
            pos[1] += -1
        elif direction == "ne":
            pos[0] += 0
            pos[1] += -1
    return tuple(pos)


black_tiles = set()

for tile in tiles_to_flip:
    pos = calc_pos(tile)
    if pos in black_tiles:
        black_tiles.remove(pos)
    else:
        black_tiles.add(pos)

print(len(black_tiles))


def get_neighbors(pos):
    neighbors = set()
    neighbors.add((pos[0] + 1, pos[1] + 1))
    neighbors.add((pos[0] + 0, pos[1] + 1))
    neighbors.add((pos[0] + 1, pos[1] + 0))
    neighbors.add((pos[0] + 0, pos[1] + -1))
    neighbors.add((pos[0] + -1, pos[1] + 0))
    neighbors.add((pos[0] + -1, pos[1] + -1))
    return neighbors


def flip_tiles(black_tiles):
    new_black_tiles = set()
    white_tiles_to_check = set()
    for black_tile in black_tiles:
        neighbors = get_neighbors(black_tile)
        black_neighbors = set()
        for n in neighbors:
            if n in black_tiles:
                black_neighbors.add(n)
            else:
                white_tiles_to_check.add(n)
        if len(black_neighbors) == 1 or len(black_neighbors) == 2:
            new_black_tiles.add(black_tile)
    for white_tile in white_tiles_to_check:
        neighbors = get_neighbors(white_tile)
        black_neighbors = neighbors.intersection(black_tiles)
        if len(black_neighbors) == 2:
            new_black_tiles.add(white_tile)

    return new_black_tiles


for x in range(100):
    black_tiles = flip_tiles(black_tiles)
    print(f"Day {x + 1}: {len(black_tiles)}")

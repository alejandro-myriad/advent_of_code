def cost(positions, align_pos):
    def single_cost(pos, new_pos):
        diff = abs(pos - new_pos)
        return (diff * (diff + 1)) / 2
    return sum(map(lambda p: single_cost(p, align_pos), positions))

def main():
    with open("input") as f:
        positions = [int(position) for position in f.read().strip().split(",")]
    print(sum(positions)/len(positions))
    lowest_cost = None
    for pos in range(max(positions)):
        new_cost = cost(positions, pos)
        if lowest_cost is None or new_cost < lowest_cost:
            lowest_cost = new_cost
        else:
            break
    print(pos, lowest_cost)

if __name__ == "__main__":
    main()

from collections import defaultdict


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
    caves = defaultdict(list)
    for line in lines:
        print(line)
        name1, name2 = line.split("-")
        caves[name1].append(name2)
        caves[name2].append(name1)
    print(caves)

    completed_paths = set()
    paths = [(["start"], False)]
    while paths:
        path, has_doubly_visited_small_cave = paths.pop()
        current_cave = path[-1]
        for next_cave in caves[current_cave]:
            if next_cave == "end":
                completed_paths.add(",".join(path + ["end"]))
            elif next_cave == "start":
                pass
            elif (
                next_cave == next_cave.upper()
                or not has_doubly_visited_small_cave
                or next_cave not in path
            ):
                has_double = has_doubly_visited_small_cave or (
                    next_cave == next_cave.lower() and next_cave in path
                )
                paths.append((path + [next_cave], has_double))

    print("\n".join(sorted(completed_paths)))
    print(len(completed_paths))


if __name__ == "__main__":
    main()

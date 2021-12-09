# Part 1: How many trees with 3 right and 1 down slope
import re
with open("input") as f:
    xpos = 0
    tree_count = 0
    for treeline in f.readlines():
        treeline = treeline.strip()
        if treeline[xpos % len(treeline)] == "#":
            tree_count += 1
        print((treeline, tree_count, xpos))
        xpos += 3
    print(tree_count)

# Part 2: How many trees with different slopes
def count_trees(treelines, xspeed, yspeed):
    xpos = 0
    ypos = 0
    tree_count = 0
    for treeline in treelines:
        if ypos % yspeed != 0:
            ypos += 1
            continue

        if treeline[xpos % len(treeline)] == "#":
            tree_count += 1
        xpos += xspeed
        ypos += 1
    return tree_count

import re
with open("input") as f:
    treelines = f.read().strip().split("\n")
    a = count_trees(treelines, 1, 1)
    b = count_trees(treelines, 3, 1)
    c = count_trees(treelines, 5, 1)
    d = count_trees(treelines, 7, 1)
    e = count_trees(treelines, 1, 2)
    print(a*b*c*d*e)

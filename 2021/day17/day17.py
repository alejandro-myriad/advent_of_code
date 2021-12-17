import sys, re
from collections import defaultdict


def main():
    if len(sys.argv) > 1:
        target_area = sys.argv[1]
    else:
        with open("input") as f:
            target_area = f.read().strip()
    groups = re.match(
        r"target area: x=(\-?\d+)..(\-?\d+), y=(\-?\d+)..(\-?\d+)$", target_area
    ).groups()
    x1, x2, y1, y2 = map(int, groups)
    print(x1, x2, y1, y2)
    v_y_max = -1 * y1 - 1
    v_y_min = y1
    steps2vy = defaultdict(list)
    for v_y in range(v_y_min, v_y_max + 1):
        y = 0
        starting_v_y = v_y
        steps = 0
        while y >= y1:
            steps += 1
            y += v_y
            v_y -= 1
            if y >= y1 and y <= y2:
                steps2vy[steps].append(starting_v_y)

    print(v_y_max, v_y_min)
    print(steps2vy)
    v_x_max = x2
    v_x_min = 0
    while ((v_x_min * (v_x_min + 1)) / 2) < x1:
        v_x_min += 1
    steps2vx = defaultdict(list)
    vx2min_steps = list()
    for v_x in range(v_x_min, v_x_max + 1):
        x = 0
        starting_v_x = v_x
        steps = 0
        while x <= x2:
            steps += 1
            x += v_x
            if v_x < 0:
                v_x += 1
            elif v_x > 0:
                v_x -= 1
            if x >= x1 and x <= x2:
                steps2vx[steps].append(starting_v_x)
                if v_x == 0:
                    vx2min_steps.append((starting_v_x, steps))
            if v_x == 0:
                break
    print(v_x_max, v_x_min)
    print(steps2vx)
    print(vx2min_steps)
    
    initial_vs = set()
    for steps, v_ys in steps2vy.items():
        for v_y in v_ys:
            for v_x in steps2vx[steps]:
                initial_vs.add((v_x, v_y))
            for v_x, min_steps in vx2min_steps:
                if steps >= min_steps:
                    initial_vs.add((v_x, v_y))
    print(initial_vs)
    print(len(initial_vs))



if __name__ == "__main__":
    main()

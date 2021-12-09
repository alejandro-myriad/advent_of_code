def grow(squid_counts, days):
    for x in range(days):
        next_gen = defaultdict(int)
        for age, count in squid_counts.items():
            if age == 0:
                next_gen[8] = count
                next_gen[6] += count
            else:
                next_gen[age - 1] += count
        squid_counts = next_gen
    return squid_counts

from collections import defaultdict
def main():
    with open("input") as f:
        squids = [int(squid) for squid in f.read().strip().split(",")]

    squid_counts = defaultdict(int)
    for squid in squids:
        squid_counts[squid] += 1
    print(sum(grow(squid_counts, 80).values()))
    print(sum(grow(squid_counts, 256).values()))

if __name__ == "__main__":
    main()

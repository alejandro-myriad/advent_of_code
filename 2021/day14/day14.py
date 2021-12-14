import sys
from collections import defaultdict


def apply_rules(rules, seq_counts):
    new_seq_counts = defaultdict(int)
    for pair, count in seq_counts.items():
        if pair in rules:
            ins = rules[pair]
            new_seq_counts["".join((pair[0], ins))] += count
            new_seq_counts["".join((ins, pair[1]))] += count
        else:
            new_seq_counts[pair] += count
    return new_seq_counts


def main():
    with open("input") as f:
        seq, rules = f.read().strip().split("\n\n")
        rules = dict(rule.split(" -> ") for rule in rules.split("\n"))

    seq_counts = defaultdict(int)
    for i in range(len(seq) - 1):
        seq_counts[seq[i:i+2]] += 1
    print(seq)
    print(seq_counts)

    for i in range(int(sys.argv[1]) if len(sys.argv) > 1 else 10):
        seq_counts = apply_rules(rules, seq_counts)
        print(sum(seq_counts.values()) + 1)

    counts = defaultdict(int)
    counts[seq[-1]] += 1
    for pair, count in seq_counts.items():
        counts[pair[0]] += count
    # print(counts)
    print(counts)
    print(seq_counts)
    print(max(counts.values()) - min(counts.values()))





if __name__ == "__main__":
    main()

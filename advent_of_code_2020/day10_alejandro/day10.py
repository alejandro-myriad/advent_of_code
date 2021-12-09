from collections import defaultdict


with open("input") as f:
    joltage_adapters = sorted(int(entry) for entry in f.read().strip().split("\n"))

print(joltage_adapters)
differences_count = defaultdict(int)
prev_adapter = 0
group_size_count = defaultdict(int)
group_size = 1
for adapter in joltage_adapters + [joltage_adapters[-1] + 3]:
    difference = adapter - prev_adapter
    differences_count[difference] += 1
    if difference == 1:
        group_size += 1
    elif difference == 3:
        group_size_count[group_size] += 1
        group_size = 1
    prev_adapter = adapter

print(differences_count)
print(differences_count[1] * differences_count[3])
print(group_size_count)
group_size_to_multiplier = {1: 1, 2: 1, 3: 2, 4: 4, 5: 7}
arrangement_counts = 1
for group_size, count in group_size_count.items():
    arrangement_counts *= group_size_to_multiplier[group_size] ** count
print(arrangement_counts)

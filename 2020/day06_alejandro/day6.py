# Part 1: Count *anyone* answered yes
def count_group(group):
    people = group.strip().split("\n")
    answers_set = set(people[0])
    for person in people:
        answers_set = answers_set.union(person)
    return len(answers_set)



with open("input") as f:
    groups = f.read().strip().split("\n\n")
    print(sum(count_group(group) for group in groups))


def count_group(group):
    people = group.strip().split("\n")
    answers_set = set(people[0])
    for person in people:
        answers_set = answers_set.intersection(person)
    return len(answers_set)



with open("input") as f:
    groups = f.read().strip().split("\n\n")
    print(sum(count_group(group) for group in groups))

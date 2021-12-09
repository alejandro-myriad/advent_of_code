# Part 1: How many bags can contain a shiny gold bag?
import regex


def to_num(number):
    return int(number) if number.isdigit() else 0


def parse_rule(rule):
    m = regex.match(r"^(.*?) bags contain ((\d+|no) ([^,.]*?) bags?[,.] ?)*?$", rule)
    return (
        m.group(1),
        list(
            (color, to_num(number))
            for color, number in zip(m.captures(4), m.captures(3))
            if to_num(number) > 0
        ),
    )


def can_hold_shiny_gold(rule_nodes, color):
    colors = {color for color, _number in rule_nodes[color]}
    if not colors:
        return False
    if "shiny gold" in colors:
        return True
    return any((can_hold_shiny_gold(rule_nodes, next_color) for next_color in colors))


def count_bags(rule_nodes, color):
    if not rule_nodes[color]:
        return 0

    return sum(number for _color, number in rule_nodes[color]) + sum(
        number * count_bags(rule_nodes, next_color) for next_color, number in rule_nodes[color]
    )


with open("input") as f:
    rule_nodes = {
        color: edges
        for color, edges in (parse_rule(rule) for rule in f.read().strip().split("\n"))
    }
    bag_count = 0
    for color in set(rule_nodes.keys()):
        if can_hold_shiny_gold(rule_nodes, color):
            bag_count += 1
    print(bag_count)
    print(count_bags(rule_nodes, "shiny gold"))

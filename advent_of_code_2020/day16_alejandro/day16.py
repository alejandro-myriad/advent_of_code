import re
from functools import partial


def parse_rule(rule):
    m = re.match(r"([^:]*): (\d*)-(\d*) or (\d*)-(\d*)", rule)
    return m.group(1), ((int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5))))




with open("input") as f:
    rules, my_ticket, tickets = f.read().strip().split("\n\n")

rules = dict(map(parse_rule, rules.split("\n")))

def get_valid_rules(value):
    valid_rules = set()
    for rule_name, rule in rules.items():
        if (value >= rule[0][0] and value <= rule[0][1]) or (
            value >= rule[1][0] and value <= rule[1][1]
        ):
            valid_rules.add(rule_name)
    return valid_rules

my_ticket = list(map(int, my_ticket.split("\n")[1].split(",")))
tickets = list(map(lambda s: tuple(map(int, s.split(","))), tickets.split("\n")[1:]))
ticket2rules = {ticket: [get_valid_rules(value) for value in ticket] for ticket in tickets}

valid_tickets = [ticket for ticket, rules in ticket2rules.items() if all(rules)]

position2rule = {}


all_valid_rules = [ticket2rules[ticket] for ticket in valid_tickets]
for position in range(len(rules)):
    possible_rules = set(rules)
    for valid_rules in all_valid_rules:
        possible_rules = possible_rules.intersection(valid_rules[position])
    position2rule[position] = possible_rules


found_rules = {}
while len(found_rules) != len(rules):
    for position, possible_rules in position2rule.items():
        if len(set(possible_rules) - set(found_rules)) == 1:
            found_rules[(set(possible_rules) - set(found_rules)).pop()] = position

print(found_rules)

departure_values = []
for rule_name, position in found_rules.items():
    if rule_name.startswith("departure"):
        departure_values.append(my_ticket[position])

import math
print(math.prod(departure_values))

from collections import defaultdict
import re

# Part 1: Value of accumulator when infinite loop detected
# def parse_instruction(instruction_line):
#     m = re.match(r"^([a-z]+) ([+-]\d+)$", instruction_line)
#     instruction, value = m.groups()
#     value = int(value)
#     return instruction, value

# with open("input") as f:
#     instructions = list(map(parse_instruction, f.read().strip().split("\n")))
#     instruction_count = defaultdict(int)
#     index = 0
#     accumulator = 0
#     while index < len(instructions):
#         instruction_count[index] += 1
#         if instruction_count[index] > 1:
#             print(accumulator)
#             break
#         instruction, value = instructions[index]
#         if instruction == "acc":
#             accumulator += value
#             index += 1
#         elif instruction == "jmp":
#             index += value
#         elif instruction == "nop":
#             index += 1
#         else:
#             raise AssertionError


# Part 2: Value of accumulator when infinite loop detected
def parse_instruction(instruction_line):
    m = re.match(r"^([a-z]+) ([+-]\d+)$", instruction_line)
    instruction, value = m.groups()
    value = int(value)
    return instruction, value


def run_instructions(instructions):
    instruction_count = defaultdict(int)
    index = 0
    accumulator = 0
    while index < len(instructions):
        instruction_count[index] += 1
        if instruction_count[index] > 1:
            return False
        instruction, value = instructions[index]
        if instruction == "acc":
            accumulator += value
            index += 1
        elif instruction == "jmp":
            index += value
        elif instruction == "nop":
            index += 1
        else:
            raise AssertionError
    return accumulator


with open("input") as f:
    instructions = list(map(parse_instruction, f.read().strip().split("\n")))
    for index in range(len(instructions)):
        new_instructions = list(instructions)
        if new_instructions[index][0] == "jmp":
            new_instructions[index] = ("nop", new_instructions[index][1])
        elif new_instructions[index][0] == "nop":
            new_instructions[index] = ("jmp", new_instructions[index][1])
        accumulator = run_instructions(new_instructions)
        if accumulator:
            print(accumulator)
            print(instructions[index - 10:index + 10])
            print(instructions[index])

import sys
C2B = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
TYPE_ID_LITERAL = 4

from functools import reduce
T2O = {
    0: sum,
    1: lambda l: reduce(lambda a,b: a * b, l),
    2: min,
    3: max,
    5: lambda l: 1 if l[0] > l[1] else 0,
    6: lambda l: 1 if l[0] < l[1] else 0,
    7: lambda l: 1 if l[0] == l[1] else 0,
}

def parse_literal(bits):
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    keep_reading = True
    literal_bits = []
    bits = bits[6:]
    while keep_reading:
        next_chunk = bits[0:5]
        bits = bits[5:]
        literal_bits.append(next_chunk[1:5])
        keep_reading = next_chunk[0] == '1'
    return version, type_id, int("".join(literal_bits), 2), bits

def parse_operator(bits):
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    length_type_id = bits[6]
    bits = bits[6:]
    remaining_bits = None
    if length_type_id == '0':
        length_of_bits = int(bits[1:16], 2)
        packets, remaining_bits = parse_bits(bits[16:], None, length_of_bits)
    elif length_type_id == '1':
        number_of_subpackets = int(bits[1:12], 2)
        packets, remaining_bits = parse_bits(bits[12:], number_of_subpackets, None)
    return version, type_id, packets, remaining_bits


def parse_bits(bits, number_of_packets, number_of_bits):
    packets = []
    if number_of_packets is not None:
        remaining_bits = None
        while number_of_packets > 0:
            number_of_packets -= 1
            type_id = int(bits[3:6], 2)
            if type_id == TYPE_ID_LITERAL:
                version, type_id, literal, remaining_bits =  parse_literal(bits)
                packets.append((version, type_id, literal))
                bits = remaining_bits
            else:
                version, type_id, subpackets, remaining_bits = parse_operator(bits)
                packets.append((version, type_id, subpackets))
                bits = remaining_bits
        return packets, remaining_bits
    elif number_of_bits is not None:
        remaining_bits = None
        while number_of_bits > 6:
            type_id = int(bits[3:6], 2)
            if type_id == TYPE_ID_LITERAL:
                version, type_id, literal, remaining_bits =  parse_literal(bits)
                packets.append((version, type_id, literal))
                number_of_bits -= len(bits) - len(remaining_bits)
                bits = remaining_bits
            else:
                version, type_id, subpackets, remaining_bits = parse_operator(bits)
                packets.append((version, type_id, subpackets))
                number_of_bits -= len(bits) - len(remaining_bits)
                bits = remaining_bits
        return packets, remaining_bits


def extract_versions(ast):
    versions = []
    for packet in ast:
        version, type_id, value = packet
        versions.append(version)
        if isinstance(value, list):
            versions.extend(extract_versions(value))
    return versions

def evaluate(ast):
    values = []
    for packet in ast:
        version, type_id, value = packet
        if type_id == TYPE_ID_LITERAL:
            values.append(value)
        else:
            f = T2O.get(type_id)
            values.append(f(evaluate(value)))
    return values

def main():
    if len(sys.argv) > 1:
        transmission = sys.argv[1]
    else:
        with open("input") as f:
            transmission = f.read().strip()
    bits = "".join(C2B[c] for c in transmission)
    ast, remaing_bits = parse_bits(bits, 1, None)
    versions = extract_versions(ast)
    print(versions)
    print(sum(versions))
    print(evaluate(ast))



if __name__ == "__main__":
    main()

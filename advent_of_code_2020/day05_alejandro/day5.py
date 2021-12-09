def row_to_num(row):
    return int(row.replace("F", "0").replace("B", "1"), 2)


def col_to_num(col):
    return int(col.replace("L", "0").replace("R", "1"), 2)


def seat_id(seat):
    row = row_to_num(seat[:7])
    col = col_to_num(seat[7:])
    return 8 * row + col


with open("input") as f:
    seat_ids = set([seat_id(seat) for seat in f.read().strip().split("\n")])
    print(max(seat_ids))
    print(set(range(min(seat_ids), max(seat_ids) + 1)) - seat_ids)

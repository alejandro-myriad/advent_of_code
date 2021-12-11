import re
import numpy as np
from functools import partial

def intify(row: str):
    return list(map(int, re.split(r"\s+", row.strip())))

def is_bingo(board):
    card, marked = board
    for row in card:
        if sum(row) == 0:
            return True
    for column in card.transpose():
        if sum(column) == 0:
            return True
    return False

def update_board(draw, board):
    card, marked = board
    if draw in card:
        card[np.where(card == draw)] = 0
        marked.append(draw)
    return card, marked

def main():
    with open("input") as f:
        sections = [section for section in f.read().strip().split("\n\n")]
        draws = list(map(int, sections[0].strip().split(",")))
        boards = []
        for section in sections[1:]:
            rows = map(intify, section.strip().split("\n"))
            boards.append((np.vstack(rows), []))
        print(draws)
        print(boards)

    winning_boards = []
    for draw in draws:
        boards = list(map(partial(update_board, draw), boards))
        print(draw)
        print(boards)
        winning_boards.extend(list(filter(is_bingo, boards)))
        boards = list(filter(lambda x: not is_bingo(x), boards))
        if not boards:
            break

    last_board = winning_boards[-1]
    print(last_board)
    card, marked = last_board
    print(card)
    print(sum(sum(card)) * draw)

if __name__ == "__main__":
    main()

import re

OPENS = "([{<"
CLOSES = ")]}>"

ILLEGAL_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

open2close = dict(zip(OPENS, CLOSES))

def get_illegal(line):
    opens = []
    closes = []
    illegal = None
    for c in line:
        if c in OPENS:
            opens.append(c)
        if c in CLOSES:
            o = opens.pop()
            if open2close[o] != c:
                return c


def get_complete_seq(line):
    opens = []
    for c in line:
        if c in OPENS:
            opens.append(c)
        if c in CLOSES:
            o = opens.pop()
            if open2close[o] != c:
                return c

    return "".join(reversed(list(map(lambda c: open2close[c], opens))))

CLOSE_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def score_completion_seq(seq):
    score = 0
    for c in seq:
        score *= 5
        score += CLOSE_SCORE[c]
    return score

def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")

    illegals = list(filter(None, map(get_illegal, lines)))
    print("syntax checker score:", sum(map(lambda i: ILLEGAL_SCORE.get(i), illegals)))
    

    incompletes = list(filter(lambda l: not get_illegal(l), lines))
    seqs = list(map(get_complete_seq, incompletes))
    scores = list(map(score_completion_seq, seqs))
    print("autocomplete score:", sorted(scores)[len(scores)//2])



if __name__ == "__main__":
    main()

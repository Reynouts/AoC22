def p1(rounds):
    points = {"x": 1, "y": 2, "z": 3}
    wins = (["a", "y"], ["b", "z"], ["c", "x"])
    score = 0
    for round in rounds:
        score += points[round[1]]
        if round in wins:
            score += 6
        elif ord(round[1]) - ord(round[0]) == 23:
            score += 3
    return score


def p2(rounds):
    c_rounds = []
    lose = {"a": "z", "b": "x", "c": "y"}
    wins = {"a": "y", "b": "z", "c": "x"}
    for round in rounds:
        if round[1] == "z":
            c_rounds.append([round[0], wins[round[0]]])
        elif round[1] == "x":
            c_rounds.append([round[0], lose[round[0]]])
        elif round[1] == "y":
            c_rounds.append([round[0], chr(ord(round[0])+23)])
    return p1(c_rounds)


def main():
    with open('day2.txt', 'r') as f:
        rounds = [round.split() for round in f.read().lower().split('\n')]
    print(f'Part 1: {p1(rounds)}')
    print(f'Part 1: {p2(rounds)}')


if __name__ == "__main__":
    main()

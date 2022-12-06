def get_score(commons):
    return sum([ord(c)-ord('a')+1 if c.islower()
                else ord(c)-ord('A')+27 for c in commons])


def main():
    with open('day3.txt', 'r') as f:
        packs = f.read().split('\n')

    commons = []
    for p in packs:
        p1 = set(p[:len(p)//2])
        p2 = set(p[len(p)//2:])
        commons.append(p1.intersection(p2).pop())
    print(f'Part 1: {get_score(commons)}')

    commons = []
    for i in range(0, 300, 3):
        commons.append(set(packs[i]).intersection(set(packs[i+1]))
                       .intersection(set(packs[i+2])).pop())
    print(f'Part 2: {get_score(commons)}')


if __name__ == "__main__":
    main()

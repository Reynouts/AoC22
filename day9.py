from math import copysign as sign


def touch(H, T):
    xdiff = H[0] - T[0]
    ydiff = H[1] - T[1]
    if xdiff > 1 or xdiff < -1 or ydiff > 1 or ydiff < -1:
        return False
    return True


def action(H, T):
    xdiff = H[0] - T[0]
    ydiff = H[1] - T[1]
    r1, r2 = 0, 0
    if xdiff != 0:
        r1 = int(sign(1, xdiff))
    if ydiff != 0:
        r2 = int(sign(1, ydiff))
    return r1, r2


def main():
    with open('day9.txt', 'r') as f:
        lines = f.read().splitlines()
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    H = [0, 0]
    T = [[0, 0] for _ in range(9)]
    p1, p2 = [(0, 0)], [(0, 0)]
    for line in lines:
        d, s = line.split()
        for _ in range(int(s)):
            H = [sum(x) for x in zip(H, dirs[d])]
            for i, t in enumerate(T):
                if i == 0:
                    leader = H
                else:
                    leader = T[i - 1]
                if not touch(leader, t):
                    T[i] = [sum(x) for x in zip(t, action(leader, t))]
                    if i == 0:
                        p1.append(tuple(T[i]))
                    if i == len(T) - 1:
                        p2.append(tuple(T[i]))

    print(f'Part1: {len(set(p1))}')
    print(f'Part2: {len(set(p2))}')


if __name__ == "__main__":
    main()
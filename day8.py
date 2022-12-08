def main():
    grid = []
    with open('day8.txt', 'r') as f:
        for line in f.read().splitlines():
            grid.append([int(c) for c in line])

    visible = 0
    highest = 0
    for y, j in enumerate(grid):
        for x, i in enumerate(j):
            l = grid[y][0:x]
            r = grid[y][x+1:]
            col = [row[x] for row in grid]
            t = col[0:y]
            b = col[y+1:]

            # part 1
            if max(l, default=-1) < i or max(r, default=-1)  < i or max(t, default=-1) < i or max(b, default=-1) < i:
                visible += 1

            # part 2
            p = 1
            for v in (reversed(l), r, reversed(t), b):
                in_view = 0
                for e in v:
                    in_view += 1
                    if e >= i:
                        break
                p *= in_view
            if p > highest:
                highest = p

    print(f'Part1: {visible}')
    print(f'Part2: {highest}')


if __name__ == "__main__":
    main()
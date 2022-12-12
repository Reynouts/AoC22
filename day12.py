def bfs(grid, current, ends, condition):
    if type(ends) != list:
        ends = [ends]
    height, width = len(grid), len(grid[0])
    steps = 0
    q = [(current, steps)]
    visited = {current}
    while q:
        current, steps = q.pop(0)
        for h in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            pos = current[0] + h[0], current[1] + h[1]
            if pos in ends:
                return steps + 1
            if pos not in visited:
                if (0 <= pos[0] < width) and (0 <= pos[1] < height) \
                        and condition(grid[pos[1]][pos[0]], grid[current[1]][current[0]]):
                    q.append((pos, steps + 1))
                    visited.add(pos)

    return 10 ** 10


def main():
    grid = []
    starts = []
    with open("day12.txt", 'r') as f:
        for y, line in enumerate(f.read().splitlines()):
            grid.append([])
            for x, c in enumerate(line):
                if c == "S":
                    start = (x, y)
                    c = "a"
                if c == "a":
                    starts.append((x, y))
                elif c == "E":
                    end = (x, y)
                    c = "z"
                grid[-1].append(c)

    print(f'Part1: {bfs(grid, start, end, lambda x, y: ord(x) - ord(y) < 2)}')
    print(f'Part2: {bfs(grid, end, starts, lambda x, y: ord(x) - ord(y) > -2)}')


if __name__ == "__main__":
    main()

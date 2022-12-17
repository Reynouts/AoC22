import re
import operator
import aocutils


def get_points(paths):
    points = {}
    for path in paths:
        for index, p in enumerate(path[:-1]):
            df = tuple(map(operator.sub, path[index + 1], path[index]))
            if df[0]:
                for i in range(min(df[0], 0), max(df[0] + 1, 1)):
                    points[(path[index][1], path[index][0] + i)] = "#"
            elif df[1]:
                for i in range(min(df[1], 0), max(df[1] + 1, 1)):
                    points[(path[index][1] + i, path[index][0])] = "#"
    return points


def drop_sand(points, height, start=(0, 500), part2=True):
    margin = height + 2
    # falling infinite or hitting the sand spawn point
    if start[0] > height + margin + 1 or start in points:
        return False
    # fall down
    if (start[0] + 1, start[1]) not in points and (start[0] + 1 != margin or not part2):
        start = start[0] + 1, start[1]
        return drop_sand(points, height, start, part2)
    # check down left
    elif (start[0] + 1, start[1] - 1) not in points and (start[0] + 1 != margin or not part2):
        start = start[0] + 1, start[1] - 1
        return drop_sand(points, height, start, part2)
    # check down right
    elif (start[0] + 1, start[1] + 1) not in points and (start[0] + 1 != margin or not part2):
        start = start[0] + 1, start[1] + 1
        return drop_sand(points, height, start, part2)
    # rest
    else:
        points[start] = "o"
        return True


def run(points, part2, offset=0):
    height = max([y for y, x in points])
    outcome = True
    original = len(points)
    while outcome:
        outcome = drop_sand(points, height, (0, 500), part2)
    return len(points) - original + offset

@aocutils.timeit
def main():
    with open("day14.txt", 'r') as f:
        paths = [[tuple(map(int, pair)) for pair in re.findall("(\d+),(\d+)", d)] for d in f.read().split("\n")]
    points = get_points(paths)
    p1 = run(points, False)
    print(f'Part1: {p1}')
    p2 = run(points, True, p1)
    print(f'Part2: {p2}')


if __name__ == "__main__":
    main()

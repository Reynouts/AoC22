from math import dist


def get_neighbours(current, border):
    nb = set()
    for h in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        new_x = current[0] + h[0]
        new_y = current[1] + h[1]
        new_z = current[2] + h[2]
        if -1 <= new_x <= border[0] and -1 <= new_y <= border[1] and -1 <= new_z <= border[2]:
            nb.add((new_x, new_y, new_z))
    return nb


def get_exposed(points1, points2):
    total_exposed = 0
    for p1 in points1:
        exposed = 6
        for p2 in points2:
            if p1 != p2 and dist(p1, p2) == 1:
                exposed -= 1
        total_exposed += exposed
    return total_exposed


def get_exterior(points):
    max_x = max([p[0] for p in points]) + 1
    max_y = max([p[1] for p in points]) + 1
    max_z = max([p[2] for p in points]) + 1

    start = -1, -1, -1
    exterior = {start}
    q = [start]
    while q:
        current = q.pop(0)
        for neighbour in get_neighbours(current, (max_x, max_y, max_z)):
            if neighbour not in exterior and neighbour not in points:
                q.append(neighbour)
                exterior.add(neighbour)
    return exterior


def main():
    with open("day18.txt", 'r') as f:
        points = [tuple(map(int, d.split(","))) for d in f.read().split('\n')]
    part1 = get_exposed(points, points)
    print("Part1:", part1)
    print("Part2:", part1 - get_exposed(points, list(get_exterior(points)) + points))


if __name__ == "__main__":
    main()
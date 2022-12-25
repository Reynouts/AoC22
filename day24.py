import math

heading_map = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
blizzard_pool = []

def run(start, end, points, steps=0, lcm=600):
    q = [(start, steps)]
    visited = set((start, steps%lcm))
    while q:
        current, steps = q.pop(0)
        if current == end:
            return steps
        steps += 1
        cb = blizzard_pool[steps%lcm]
        for h in heading_map:
            nb = current[0] + heading_map[h][0], current[1] + heading_map[h][1]
            if nb in points and points[nb] == "." and nb not in [b[0] for b in cb]:
                if (nb, steps%lcm) not in visited:
                    q.append((nb, steps))
                    visited.add((nb, steps%lcm))
        if current not in [b[0] for b in cb] and (current, steps%lcm) not in visited:
            q.append((current, steps))
            visited.add((current, steps%lcm))
    return -1


def build_blizzard_map(points, lcm):
    for _ in range(lcm-1):
        new_blizzards = []
        for b in blizzard_pool[-1]:
            p, h = b
            np = p[0] + heading_map[h][0], p[1] + heading_map[h][1]
            if points[np] == "#":
                #wrap around..?
                dx, dy = heading_map[h]
                dx *= -1
                dy *= -1
                x, y = np
                x += dx
                y += dy
                while points[(x, y)] != "#":
                    x += dx
                    y += dy
                new_blizzards.append(((x - dx, y - dy), h))
            else:
                new_blizzards.append((np, h))
        blizzard_pool.append(new_blizzards)


def main():
    with open("day24.txt", 'r') as f:
        data = f.read()
    points = dict()
    blizzards = []
    for y, line in enumerate(data.split("\n")):
        for x, e in enumerate(line):
            if e in heading_map:
                blizzards.append(((x,y), e))
                e = "."
            points[x,y] = e
            if y == 0 and e == ".":
                start = (x, y)
            if y == len(data.split("\n"))-1 and e == ".":
                end = (x, y)
    lcm = math.lcm(y-1,x-1)
    blizzard_pool.append(blizzards)
    build_blizzard_map(points, lcm)
    steps = run(start, end, points, 0, lcm)
    print("Part1:",steps)
    steps = run(end, start, points, steps, lcm)
    steps = run(start, end, points, steps, lcm)
    print("Part2:",steps)


if __name__ == "__main__":
    main()

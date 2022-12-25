import re


class Tile:
    def __init__(self, x, y, wall):
        self.x = x
        self.y = y
        self.wall = wall
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.rot = dict()

    def location(self):
        return self.x, self.y


class Player:
    headings = ["right", "bottom", "left", "top"]

    def __init__(self, current, heading_index=0):
        self.current = current
        self.heading_index = heading_index

    def get_score(self):
        return 1000*(self.current.y+1)+4*(self.current.x+1)+self.heading_index

    def rotate(self, argument):
        if argument == "R":
            nhead = self.heading_index + 1
        elif argument == "L":
            nhead = self.heading_index - 1
        self.heading_index = nhead % len(Player.headings)

    def heading(self):
        return Player.headings[self.heading_index]

    def move(self):
        old_place = self.current
        old_heading_index = self.heading_index
        self.current = {"right": self.current.right, "left": self.current.left,
                        "top": self.current.top, "bottom": self.current.bottom}[self.heading()]
        if self.current.wall:
            self.current = old_place
        else:
            if old_heading_index in old_place.rot:
                self.heading_index = old_place.rot[old_heading_index]
            else:
                self.heading_index = old_heading_index


def create_tiles(grid):
    tiles = {}
    for t in grid:
        wall = False
        if grid[t] == "#":
            wall = True
        tiles[t] = Tile(*t, wall)
    return tiles


def set_neighbours(tiles):
    for t in tiles:
        x, y = t
        # set right neighbour
        nx = x
        if (x + 1, y) not in tiles:
            while (nx, y) in tiles:
                nx -= 1
        tiles[t].right = tiles[(nx + 1, y)]
        # set left neighbour
        nx = x
        if (x - 1, y) not in tiles:
            nx = x + 1
            while (nx, y) in tiles:
                nx += 1
        tiles[t].left = tiles[(nx - 1, y)]
        # set top neighbour
        ny = y
        if (x, y - 1) not in tiles:
            ny = ny + 1
            while (x, ny) in tiles:
                ny += 1
        tiles[t].top = tiles[(x, ny - 1)]
        # set bottom neighbour
        ny = y
        if (x, y + 1) not in tiles:
            ny = ny - 1
            while (x, ny) in tiles:
                ny -= 1
        tiles[t].bottom = tiles[(x, ny + 1)]


def marksides(grid):
        for test in helper.split('\n\n')[1:]:
            start, inc = test.split("\n")
            xs1, ys1, dir, xs2, ys2, rotate = list(map(int, re.findall("\d+", start)))
            x1, y1, x2, y2 = list(map(int, re.findall("-?\d+", inc)))

            for _ in range(50):
                if dir == 0:
                    grid[(xs1, ys1)].right = grid[(xs2, ys2)]
                elif dir == 1:
                    grid[(xs1, ys1)].bottom = grid[(xs2, ys2)]
                elif dir == 2:
                    grid[(xs1, ys1)].left = grid[(xs2, ys2)]
                elif dir == 3:
                    grid[(xs1, ys1)].top = grid[(xs2, ys2)]
                grid[(xs1, ys1)].rot[int(dir)] = int(rotate)
                xs1 += x1
                ys1 += y1
                xs2 += x2
                ys2 += y2


def run(instructions, tiles, start_pos):
    p = Player(tiles[start_pos])

    for instruction in re.split('(\d+)', instructions):
        if instruction != "":
            if instruction.isdigit():
                for _ in range(int(instruction)):
                    p.move()
            else:
                p.rotate(instruction)

    return p.get_score()


def main():
    with open("day22.txt", 'r') as f:
        field, instructions = f.read().split('\n\n')
    grid = {}
    start_pos = None
    for y, row in enumerate(field.split("\n")):
        for x, e in enumerate(row):
            if e != " ":
                grid[(x, y)] = e
                if not start_pos:
                    start_pos = (x, y)

    tiles = create_tiles(grid)
    set_neighbours(tiles)
    print("Part1:", run(instructions, tiles, start_pos))
    marksides(tiles)
    print("Part2:", run(instructions, tiles, start_pos))


helper = """
start_tile start_direction target_tile needed_rotation
dx1,dy1 dx2,dy2

50,0 2 0,149 0
0,1 0,-1

0,100 2 50,49 0
0,1 0,-1

50,0 3 0,150 0
1,0 0,1

0,150 2 50,0 1
0,1 1,0

0,100 3 50,50 0
1,0 0,1

50,50 2 0,100 1
0,1 1,0

100,0 3 0,199 3
1,0 1,0

0,199 1 100,0 1
1,0 1,0

149,0 0 99,149 2
0,1 0,-1

99,149 0 149,0 2
0,-1 0,1

100,49 1 99,50 2
1,0 0,1

99,50 0 100,49 3
0, 1 1,0

50,149 1 49,150 2
1,0 0,1

49,150 0 50,149 3
0,1 1,0"""


if __name__ == "__main__":
    main()



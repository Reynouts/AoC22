class Elf:
    def __init__(self, position):
        self.position = position
        self.heading_index = 0
        self.proposed = None

    def get_proposed(self, points):
        self.proposed = None
        cheading_index = self.heading_index
        directions = ((( 0, -1), (-1, -1), ( 1, -1)),
                      (( 0,  1), ( 1,  1), (-1,  1)),
                      ((-1,  0), (-1, -1), (-1,  1)),
                      (( 1,  0), ( 1, -1), ( 1,  1)))
        must_expand = False
        for d in directions:
            for h in d:
                if (self.position[0] + h[0], self.position[1] + h[1]) in points:
                    must_expand = True
                    break
            if must_expand:
                break
        if must_expand:
            for _ in range(len(directions)):
                new_d = [(self.position[0] + h[0], self.position[1] + h[1]) for h in directions[cheading_index]]
                next = False
                for i in new_d:
                    if i in points:
                        next = True
                        break
                if not next:
                    self.heading_index = (self.heading_index + 1) % len(directions)
                    self.proposed = new_d[0]
                    return new_d[0]
                cheading_index = (cheading_index + 1) %len(directions)
        self.heading_index = (self.heading_index + 1) % len(directions)
        return None

def round(elves):
    allowed_to_move = {}
    points = {e.position for e in elves}
    for e in elves:
        proposed = e.get_proposed(points)
        if proposed:
            if proposed in allowed_to_move:
                allowed_to_move[proposed].append(e)
            else:
                allowed_to_move[proposed] = [e]
    still_moving = False
    for p in allowed_to_move:
        if len(allowed_to_move[p]) == 1:
            allowed_to_move[p][0].position = p
            still_moving = True
    return still_moving


def main():
    with open("day23.txt", 'r') as f:
        elves = [Elf((x, y)) for y, line in enumerate(f.read().split('\n')) for x, e in enumerate(line) if e == "#"]

    for cycle in range(10**10):
        still_moving = round(elves)
        if not still_moving:
            print("Part2:", cycle+1)
            break
        if cycle == 9:
            x = [elf.position[0] for elf in elves]
            y = [elf.position[1] for elf in elves]
            total = ((max(x) - min(x) + 1) * (max(y) - min(y) + 1)) - len(elves)
            print("Part1:", total)







if __name__ == "__main__":
    main()

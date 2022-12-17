import re


class Ranges:
    def __init__(self, y):
        self.ranges = []
        self.y = y
        self.n_beacons = 0

    def merge(self, range):
        new_range = range
        new_ranges = []
        for r in self.ranges:
            if overlap(r, new_range):
                new_range = (min(r[0], new_range[0]), max(r[1], new_range[1]))
            else:
                new_ranges.append(r)
        new_ranges.append(new_range)
        self.ranges = new_ranges


def overlap(r1, r2):
    if (r1[0] <= r2[0] <= r1[1]) or (r2[0] <= r1[0] <= r2[1]) or \
            (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1]):
        return True
    return False


def main():
    with open("day15.txt", 'r') as f:
        data = [[int(n) for n in re.findall("-?\d+", d)] for d in f.read().split('\n')]
    p1 = 2000000
    p2 = 4000000

    total_ranges = [Ranges(y) for y in range(p2 + 1)]
    range_p1 = Ranges(p1)
    for d in data:
        sensor = (d[0], d[1])
        beacon = (d[2], d[3])
        total_ranges[beacon[1]].n_beacons += 1
        perception_range = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        for target_y in range(max(sensor[1] - perception_range, 0), min(sensor[1] + perception_range, p2) + 1):
            distance_to_target = abs(target_y - sensor[1])
            if distance_to_target <= perception_range:
                overshoot = perception_range - distance_to_target
                nx_min = sensor[0] - overshoot
                nx_max = sensor[0] + overshoot
                total_ranges[target_y].merge((max(0, nx_min), min(nx_max, p2)))
                if target_y == p1:
                    range_p1.merge((nx_min, nx_max + 1))

    print(f'Part1: {range_p1.ranges[0][1] - range_p1.ranges[0][0] - range_p1.n_beacons}')

    for c in total_ranges:
        if len(c.ranges) > 1:
            print(f'Part2: {((c.ranges[0][1] + 1) * p2) + c.y}')
            return


if __name__ == "__main__":
    main()

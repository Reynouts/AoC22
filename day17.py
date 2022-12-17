def get_top(points, floor, margin=5):
    return {(p[0], p[1] - floor) for p in points if p[1] >= floor - margin}


def main():
    with open("day17.txt", 'r') as f:
        flow = f.read().split('\n')[0]

    block_prototypes = (((2, 3), (3, 3), (4, 3), (5, 3)),
                        ((3, 3), (3, 4), (3, 5), (2, 4), (4, 4)),
                        ((2, 3), (3, 3), (4, 3), (4, 4), (4, 5)),
                        ((2, 3), (2, 4), (2, 5), (2, 6)),
                        ((2, 3), (2, 4), (3, 3), (3, 4)))

    directions = {">": (1, 0), "<": (-1, 0)}
    floor = -1
    width = 7
    field = {(i, -1) for i in range(-1, width+1)}

    blocks = []
    pattern = []
    check_from = 1730  # MANUAL MAGIC
    old_floor, old_blocks, flow_ptr = -1, 0, 0
    second = True
    while True:
        for pt in block_prototypes:
            if len(blocks) == 2022:
                print("Part1:", floor + 1)
            block = [(p[0], p[1] + floor + 1) for p in pt]
            rest = False
            while not rest:
                # left/right
                instruction = directions[flow[flow_ptr]]
                flow_ptr = (flow_ptr+1)%len(flow)
                potential_move = [(p[0] + instruction[0], p[1]) for p in block]
                if not {-1, width} & set((p[0] for p in potential_move)):
                    if not field & set(potential_move):
                        block = potential_move
                # down
                potential_move = [(p[0], p[1] - 1) for p in block]
                if not field & set(potential_move):
                    block = potential_move
                # settle
                else:
                    for p in block:
                        field.add(p)
                    blocks.append(block)
                    break
            floor = max((point[1] for point in field))
            # part 2 checks
            if len(blocks) == check_from:
                # get top status after specified block falls
                pattern = get_top(field, floor)
                old_floor = floor
                old_blocks = len(blocks)
                #print("pattern initialized", floor, len(blocks))
            elif pattern:
                new_pattern = get_top(field, floor)
                if pattern == new_pattern:
                    #print(f"found pattern after {len(blocks)}, difference {len(blocks) - old_blocks}")
                    #print(f"\tfloor went from {old_floor} to {floor}; {floor - old_floor}")
                    if second:
                        print("Part2:", (((1000000000000 - old_blocks) // (len(blocks) - old_blocks)) * (
                                floor - old_floor)) + old_floor + 1)
                        return
                    pattern = new_pattern
                    old_floor = floor
                    old_blocks = len(blocks)
                    second = True


if __name__ == "__main__":
    main()

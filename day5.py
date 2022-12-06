import re


def get_stacks(config):
    stacks = [[] for _ in range(int((re.findall("\d+", config[-1])[-1])))]
    for line in config[len(config)-2::-1]:
        for i, c in enumerate(line):
            if c.isalpha():
                stacks[i//4].append(line[i])
    print(stacks)
    return stacks


def part1(stacks, amount, fr, to):
    for a in range(amount):
        stacks[to - 1].append(stacks[fr - 1].pop())
    return stacks


def part2(stacks, amount, fr, to):
    stacks[to - 1] = stacks[to - 1] + stacks[fr - 1][-amount:]
    stacks[fr - 1] = stacks[fr - 1][:-amount]
    return stacks


def get_front_crates(stacks):
    return [stack[-1] for stack in stacks]


def main():
    with open('day5.txt', 'r') as f:
        config, instructions = f.read().split('\n\n')

    stacksp1 = get_stacks(config.split("\n"))
    stacksp2 = get_stacks(config.split("\n"))

    for i in instructions.split('\n'):
        numbers = list(map(int, re.findall("\d+", i)))
        if len(numbers) == 3:
            stacksp1 = part1(stacksp1, *numbers)
            stacksp2 = part2(stacksp2, *numbers)
    print("Part1: " + "".join(get_front_crates(stacksp1)))
    print("Part2: " + "".join(get_front_crates(stacksp2)))

if __name__ == "__main__":
    main()

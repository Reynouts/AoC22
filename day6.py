import re


def get_start(data, offset):
    for i, c in enumerate(data):
        if len(set(data[i:i + offset])) == offset:
            return i + offset


def main():
    with open('day6.txt', 'r') as f:
        data = f.read()
    print(f'Part1: {get_start(data, 4)}')
    print(f'Part2: {get_start(data, 14)}')


if __name__ == "__main__":
    main()
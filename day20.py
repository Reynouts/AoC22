from dataclasses import dataclass


@dataclass
class Number:
    number: int
    original: int
    position: int


def decrypt(numbers):
    for n1 in numbers:
        new_position = (n1.position + n1.number) % (len(numbers) - 1)
        if new_position > n1.position:
            for n2 in numbers:
                if n1 != n2 and n1.position < n2.position <= new_position:
                    n2.position -= 1
        elif new_position < n1.position:
            for n2 in numbers:
                if n1 != n2 and n1.position >= n2.position >= new_position:
                    n2.position += 1
        n1.position = new_position


def get_grove_coordinates(numbers):
    checkpos = -1
    for n in numbers:
        if n.number == 0:
            checkpos = n.position
            break
    indices = [(checkpos + i) % len(numbers) for i in (1000, 2000, 3000)]
    return sum([n.number for n in numbers if n.position in indices])


def main():
    with open("day20.txt", 'r') as f:
        data = list(map(int, f.read().split('\n')))
    numbers = [Number(n, index, index) for index, n in enumerate(data)]

    decrypt(numbers)
    print("Part1:", get_grove_coordinates(numbers))

    for n in numbers:
        n.position = n.original
        n.number = n.number * 811589153

    for i in range(10):
        decrypt(numbers)
    print("Part2:", get_grove_coordinates(numbers))


if __name__ == "__main__":
    main()

import functools


def compare(list1, list2):
    for i in range(min(len(list1), len(list2))):
        if type(list1[i]) is not list and type(list2[i]) is not list:
            if list1[i] == list2[i]:
                continue
            if list1[i] < list2[i]:
                return True
            return False
        else:
            l1, l2 = list1[i], list2[i]
            if type(l1) is not list:
                l1 = [l1]
            if type(l2) is not list:
                l2 = [l2]
            result = compare(l1, l2)
            if result is None:
                continue
            return result
    if len(list1) < len(list2):
        return True
    elif len(list1) > len(list2):
        return False
    else:
        return None


def cmp(list1, list2):
    res = compare(list1, list2)
    if res == True:
        return -1
    if res == False:
        return 1
    else:
        return 0


def main():
    with open("day13.txt", 'r') as f:
        pairs = [list(map(eval, pairs.split("\n"))) for pairs in f.read().split("\n\n")]

    print(f'Part1: {sum([index + 1 for index, packet in enumerate(pairs) if compare(*packet)])}')

    dividers = [[[6]], [[2]]]
    p2 = sorted(dividers + [packet for pair in pairs for packet in pair], key=functools.cmp_to_key(cmp))
    print(f'Part2: {(p2.index(dividers[0]) + 1) * (p2.index(dividers[1]) + 1)}')


if __name__ == "__main__":
    main()

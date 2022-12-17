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


def main():
    with open("day13.txt", 'r') as f:
        pairs = [list(map(eval, pairs.split("\n"))) for pairs in f.read().split("\n\n")]

    print(f'Part1: {sum([index + 1 for index, packet in enumerate(pairs) if compare(*packet)])}')

    dividers = [[[6]], [[2]]]
    s1, s2 = 1, 1
    for i in dividers + [packet for pair in pairs for packet in pair]:
        if compare(i, dividers[0]):
            s1 += 1
        if compare(i, dividers[1]):
            s2 += 1
    print(f'Part2: {s1*s2}')


if __name__ == "__main__":
    main()

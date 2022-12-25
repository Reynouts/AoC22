snafu_map = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


def snafu_to_dec(s):
    return sum([snafu_map[c] * (5 ** i) for i, c in enumerate(reversed(s))])


def dec_to_snafu(d):
    if d == 0:
        return ""
    return dec_to_snafu((d + 2) // 5) + list(snafu_map)[(d + 2) % 5]


def main():
    with open("day25.txt", 'r') as f:
        print(dec_to_snafu(sum([snafu_to_dec(s) for s in f.read().split("\n")])))


if __name__ == "__main__":
    main()

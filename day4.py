import re

def main():
    with open('day4.txt', 'r') as f:
        pairs = f.read().split('\n')

    p1 = 0
    p2 = 0
    for pair in pairs:
        x1, y1, x2, y2 = map(int, (re.findall("\d+", pair)))
        if (x1 >= x2 and y1 <= y2) or (x2 >= x1 and y2 <= y1):
            p1 += 1
        if (x1 < x2 and y1 < x2) or (x2 < x1 and y2 < x1):
            continue
        else:
            p2 += 1
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()

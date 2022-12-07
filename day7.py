import operator

class Directory():
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.dirs = set()
        self.files = set()

    def get_size(self):
        return sum([o.get_size() for o in self.files|self.dirs])

class File():
    def __init__(self, name, parent, size):
        self.parent = parent
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


def traverse(visited, current, initial, op, func, check):
    totals = initial[:]
    if current not in visited:
        if op(current.get_size(), check):
            totals.append(current.get_size())
        visited.add(current)
        for dir in current.dirs:
            totals.append(traverse(visited, dir, initial, op, func, check))
    return func(totals)


def main():
    with open('day7.txt', 'r') as f:
        data = f.read().split('\n')

    current = None
    root = None
    for d in data:
        if d == "$ cd ..":
            current = current.parent
        elif d == "$ cd /":
            if root == None:
                root = Directory(d.split()[-1], current)
            current = root
        elif "$ cd " in d:
            for dir in current.dirs:
                if dir.name == d.split()[-1]:
                    current = dir
                    break
        elif "$" not in d:
            if "dir " in d:
                current.dirs.add(Directory(d.split()[-1], current))
            else:
                size, name = d.split()
                current.files.add(File(name, current, int(size)))

    max_size = 100000
    print(f'Part1: {traverse(set(), root, [], operator.le, sum, max_size)}')
    need = 30000000 - (70000000 - root.get_size())
    print(f'Part2: {traverse(set(), root, [10**10], operator.ge, min, need)}')


if __name__ == "__main__":
    main()
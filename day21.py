class Monkey:
    def __init__(self, name, value, left, right):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

    def get_number(self):
        if self.left is None and self.right is None:
            return self.value
        l = self.left.get_number()
        r = self.right.get_number()

        if self.value == "*":
            return l * r
        if self.value == "+":
            return l + r
        if self.value == "/":
            return l // r
        if self.value == "-":
            return l - r
        if self.value == "=":
            return l - r

    def query(self, name):
        if self.name == name:
            return True
        elif not self.left and not self.right:
            return False
        if self.left:
            r = self.left.query(name)
        if self.right:
            l = self.right.query(name)
        return l or r

    def backtrack(self, name, answer=0):
        if self.name == name:
            return int(answer)
        switch = False
        if self.left.query(name):
            known = self.right.get_number()
            subtree = self.left
        elif self.right.query(name):
            known = self.left.get_number()
            subtree = self.right
            switch = True

        if self.value == "*":
            nxt = answer / known
        if self.value == "+":
            nxt = answer - known
        if self.value == "/":
            nxt = answer * known
            if switch:
                nxt = known // answer
        if self.value == "-":
            nxt = answer + known
            if switch:
                nxt = -(answer - known)
        if self.value == "=":
            nxt = known

        return subtree.backtrack(name, nxt)


def main():
    with open("day21.txt", 'r') as f:
        data = f.read().split('\n')
    monkeys = {}
    for d in data:
        name, rest = d.split(":")
        rest = rest.split()
        left = None
        right = None
        if len(rest) == 1:
            value = int(rest[0])
        else:
            value = rest[1]
            left = rest[0]
            right = rest[2]
        monkeys[name] = Monkey(name, value, left, right)

    for m in monkeys:
        if monkeys[m].left:
            monkeys[m].left = monkeys[monkeys[m].left]
            monkeys[m].right = monkeys[monkeys[m].right]

    print("Part1:",monkeys["root"].get_number())

    monkeys["root"].value = "="
    print("Part2:",monkeys["root"].backtrack("humn"))



if __name__ == "__main__":
    main()

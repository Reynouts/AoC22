import re
from dataclasses import dataclass
from typing import Callable


@dataclass
class Config:
    rounds: int
    func: Callable


class Monkey:
    div = 1

    def __init__(self, s):
        info = s.split("\n")
        self.amount = 0
        self.items = list(map(int, re.findall("\d+", info[1])))
        self.operation = info[2].split("=")[-1]
        self.test = int(re.findall("\d+", info[3])[0])
        self.throw = int(re.findall("\d+", info[5])[0]), int(re.findall("\d+", info[4])[0])
        Monkey.div *= self.test

    def mod(op, v=3):
        return op // v

    def divide(op):
        return op % Monkey.div

    def evaluate(self, func):
        to_monkey = []
        for index, item in enumerate(self.items):
            old = self.items[index]
            self.items[index] = func(eval(self.operation))
            to_monkey.append((self.throw[int(not self.items[index] % self.test)], self.items[index]))
            self.amount += 1
        self.items = []
        return to_monkey


def main():
    with open('day11.txt', 'r') as f:
        instructions = f.read().split("\n\n")

    parts = (Config(20, Monkey.mod), Config(10000, Monkey.divide))
    for index, part in enumerate(parts):
        monkeys = [Monkey(i) for i in instructions]
        for _ in range(part.rounds):
            for m in monkeys:
                to_monkey = m.evaluate(part.func)
                for item in to_monkey:
                    monkeys[item[0]].items.append(item[1])
        amounts = sorted([m.amount for m in monkeys])[-2:]
        print(f'Part{index + 1}: {amounts[0] * amounts[1]}')


if __name__ == "__main__":
    main()

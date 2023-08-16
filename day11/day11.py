import re

class Monkey:
  def __init__(self, items, operation_line, divisor, if_true, if_false):
    self.items = items
    self.divisor = divisor
    self.if_true = if_true
    self.if_false = if_false
    self.test = lambda x: if_true if x % divisor == 0 else if_false
    if operation_line[5] == "old":
      self.operation = lambda x: x**2 if operation_line[4] == "*" else x + x
    else:
      self.operation = lambda x: x * int(operation_line[5]) if operation_line[4] == "*" else x + int(operation_line[5])
    self.inspections = 0


def parse_monkeys(lines: str) -> list[Monkey]:
  monkey_info = [str.split(line, "\n") for line in lines.split("\n\n")]
  monkeys = []

  for i, info in enumerate(monkey_info):
    items = [int(el.replace(',', '')) for el in info[1].split()[2:]]
    operation_line = info[2].split()
    divisor = int(info[3].split()[3])
    if_true = int(info[4].split()[5])
    if_false = int(info[5].split()[5])

    monkeys.append(Monkey(items, operation_line, divisor, if_true, if_false))
  return monkeys


def monkey_business(lines, iterations, divide=True):
  monkeys = parse_monkeys(lines)
  if not divide:
    divisors = 1
    for m in monkeys: divisors *= m.divisor

  for iter in range(iterations):
    for i, monkey in enumerate(monkeys):
      for item in monkey.items:
        monkey.inspections += 1
        worry = monkey.operation(item)
        if divide:
          worry //= 3
        elif worry >= divisors:
          worry %= divisors
        which_monkey = monkey.test(worry)
        monkeys[which_monkey].items.append(worry)
      monkey.items = []

  monkeys.sort(key=lambda x: x.inspections)
  print(monkeys[-1].inspections * monkeys[-2].inspections)

if __name__ == "__main__":
  with open("day11/input.txt") as file:
    lines = file.read()

  monkey_business(lines, 20)
  monkey_business(lines, 10000, False)
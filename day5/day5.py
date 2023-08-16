import copy
import time

def time_it(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    res = func(*args, **kwargs)
    print("TIME: ",  time.time() - start)
    return res
  return wrapper
  
def find_last_boxes_line(lines):
  for i, line in enumerate(lines):
    for c in line:
      if c.isnumeric():
        return i-1
  return None

def get_box_stacks(lines):
  height = find_last_boxes_line(lines)
  stacks = [[] for _ in range(len(lines[0])//4)]

  for line in lines[:height+1]:
    for i in range(1, len(line), 4):
      if line[i].isalpha():
        stacks[i//4].insert(0, line[i])
  return stacks

@time_it
def follow_instructions(stacks, instructions, is_CrateMover9001=False):
  for instruction in instructions:
    if instruction[0] != 'm': continue
    _, how_many, _, from_stack, _, to_stack = instruction.split()
    how_many, from_stack, to_stack = int(how_many), int(from_stack) - 1, int(to_stack) - 1

    if not is_CrateMover9001:
      for _ in range(how_many):
        stacks[to_stack].append(stacks[from_stack].pop())
    else:
      n = len(stacks[from_stack])
      stacks[to_stack].extend(stacks[from_stack][n-how_many:])
      stacks[from_stack] = stacks[from_stack][:n-how_many]

  ans = ""
  for stack in stacks:
    if stack:
      ans += stack[-1]

  return ans


if __name__ == "__main__":
  with open('day5/input.txt') as file:
    lines = file.readlines()
  stacks1 = get_box_stacks(lines)
  stacks2 = copy.deepcopy(stacks1)
  print(follow_instructions(stacks1, lines))
  print(follow_instructions(stacks2, lines, is_CrateMover9001=True))
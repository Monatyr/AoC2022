def draw_and_calc(cycle, x):
  if((cycle - 1) % 40 == 0): print()
  print('#', end='') if abs(x - (cycle%40 - 1)) <= 1 else print(' ', end='')
  if (cycle + 20) % 40 == 0:
    return cycle * x
  return 0

def draw_crt(lines):
  cycle, x, total_strength = 0, 1, 0

  for line in lines:
    cmds = line.split()
    cycle += 1
    total_strength += draw_and_calc(cycle, x)
    if cmds[0] == "addx":
      cycle += 1
      total_strength += draw_and_calc(cycle, x)
      x += int(cmds[1])
  print()
  return total_strength

if __name__ == "__main__":
  with open("day10/input.txt") as file:
    lines = list(map(str.strip, file.readlines()))

print(draw_crt(lines))

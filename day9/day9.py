import operator

cmd_dir = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

def follow_part(curr_head, tail):
  if abs(tail[0] - curr_head[0]) <= 1 and abs(tail[1] - curr_head[1]) <= 1:
    return tail
  diff = tuple(map(operator.sub, curr_head, tail))
  diff = (diff[0]//2 if abs(diff[0])==2 else diff[0], diff[1]//2 if abs(diff[1])==2 else diff[1])
  return tuple(map(operator.add, tail, diff))


def rope_solution(lines, n):
  unique_squares = 1
  visited = {(0,0)}
  current = [(0, 0) for _ in range(n)]

  for cmd in lines:
    direction, times = cmd.split(" ")
    times = int(times)
    move = cmd_dir[direction]

    for _ in range(times):
      current[0] = tuple(map(operator.add, current[0], move))
      for i in range(1, len(current)):
        current[i] = follow_part(current[i-1], current[i])
        if i == len(current) - 1 and current[i] not in visited:
          unique_squares += 1
          visited.add(current[i])

  return unique_squares


if __name__ == "__main__":
  with open("day9/input.txt") as file:
    lines = list(map(str.strip, file.readlines()))

  print(rope_solution(lines, 2)) #ex. 1
  print(rope_solution(lines, 10)) # ex. 2

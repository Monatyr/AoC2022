def find_start(grid: list[str]):
  for i, line in enumerate(grid):
    for j, el in enumerate(line):
      if el == 'S': return (i,j)
  return None

def find_finish(grid: list[str]):
  for i, line in enumerate(grid):
    for j, el in enumerate(line):
      if el == 'E': return (i,j)
  return None


def special_field_neighbor(grid, pos_value, neigh_value):
  if pos_value == 'S' and (neigh_value == 'a' or neigh_value == 'b'):
    return True
  return (pos_value == 'z' or pos_value == 'y') and neigh_value == 'E'


def check_if_climbable(grid, pos, neigh):
  pos_value, neigh_value = grid[pos[0]][pos[1]], grid[neigh[0]][neigh[1]]
  if special_field_neighbor(grid, pos_value, neigh_value): return True
  if ord(neigh_value) < ord(pos_value) and neigh_value != 'E': return True
  return abs(ord(pos_value) - ord(neigh_value)) <= 1


def bfs(grid, start_pos=None):
  height, width = len(grid), len(grid[0])
  if not start_pos:
    start_pos = find_start(grid)
  end_pos = find_finish(grid)
  visited = set()
  to_visit = [start_pos]
  parents = [[(-1, -1) for _ in range(width)] for _ in range(height)]
  steps = 0

  while to_visit:
    pos = to_visit.pop(0)
    if pos == end_pos:
      break
    if pos in visited:
      continue
    visited.add(pos)

    if pos[0] > 0 and (pos[0]-1, pos[1]) not in visited and check_if_climbable(grid, pos, (pos[0]-1, pos[1])):
      to_visit.append((pos[0]-1, pos[1]))
      parents[pos[0]-1][pos[1]] = pos
    if pos[0] < height - 1 and (pos[0]+1, pos[1]) not in visited and check_if_climbable(grid, pos, (pos[0]+1, pos[1])):
      to_visit.append((pos[0]+1, pos[1]))
      parents[pos[0]+1][pos[1]] = pos
    if pos[1] > 0 and (pos[0], pos[1]-1) not in visited and check_if_climbable(grid, pos, (pos[0], pos[1]-1)):
      to_visit.append((pos[0], pos[1]-1))
      parents[pos[0]][pos[1]-1] = pos
    if pos[1] < width - 1 and (pos[0], pos[1]+1) not in visited and check_if_climbable(grid, pos, (pos[0], pos[1]+1)):
      to_visit.append((pos[0], pos[1]+1))
      parents[pos[0]][pos[1]+1] = pos

  if pos != end_pos:
    return float('+inf')
  while pos != start_pos:
    steps += 1
    pos = parents[pos[0]][pos[1]]
  return steps


def multiple_starts(grid):
  num = 0
  min_steps = float('+inf')
  for i, line in enumerate(grid):
    for j, el in enumerate(line):
      if el == 'a' or el == 'S':
        min_steps = min(min_steps, bfs(grid, (i,j)))
  return min_steps


if __name__ == "__main__":
  with open('day12/input.txt') as file:
    lines = list(map(str.strip, file.readlines()))
  
  print(bfs(lines))               #ex1
  print(multiple_starts(lines))   #ex2 should be implemented end_pos as starting and find the first 'a' value square.
                                  #too lazy to do it though ;). This way the code works without altering in both excercises. 

  
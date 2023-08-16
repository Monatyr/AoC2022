def find_map_size(paths, floor=False):
  max_value = 0
  for path in paths:
    for coords in path:
      max_value = (max(max_value, max(coords[0], coords[1])))
  if not floor:
    return max_value + 1 #for safety
  return max_value + 100


def prepare_map(paths, floor=False):
  size = find_map_size(paths)
  plain = [['.' for _ in range(size)] for _ in range(size)]

  for path in paths:
    for i in range(len(path)-1):
      if path[i][0] == path[i+1][0]: #SAME X [0]
        min_val, max_val = min(path[i][1], path[i+1][1]), max(path[i][1], path[i+1][1])
        for j in range(min_val, max_val+1):
          plain[j][path[i][0]] = '#'
      else: #SAME Y [1]
        min_val, max_val = min(path[i][0], path[i+1][0]), max(path[i][0], path[i+1][0])
        for j in range(min_val, max_val+1):
          plain[path[i][1]][j] = '#'
  plain[0][500] = '+'
  return plain


def simulate_sand(plain, start_x, floor=False):
  n, grains, flag = len(plain), 0, True

  while flag:
    curr_sand = (0, start_x)
    while True:
      if not floor and curr_sand[0] >= n-1:
        flag = False
        break
      if plain[curr_sand[0]+1][curr_sand[1]] == '.':
        curr_sand = (curr_sand[0]+1, curr_sand[1])
      elif plain[curr_sand[0]+1][curr_sand[1]-1] == '.': #not checking if in bounds!
        curr_sand = (curr_sand[0]+1, curr_sand[1]-1)
      elif plain[curr_sand[0]+1][curr_sand[1]+1] == '.': #not checking if in bounds!
        curr_sand = (curr_sand[0]+1, curr_sand[1]+1)
      else:
        plain[curr_sand[0]][curr_sand[1]] = 'o'
        grains += 1
        if floor and curr_sand[0] == 0:
          flag = False
        break
  return grains


def find_lowest_point(paths):
  max_value = 0
  for path in paths:
    for coords in path:
      max_value = max(max_value, coords[1])
  return max_value


def plain_with_floor(plain, paths):
  for row in plain:
    row.extend(['.' for _ in range(200)])
  lowest_point = find_lowest_point(paths)
  if len(plain) >= lowest_point:
    for i in range(len(plain[0])):
      plain[lowest_point+2][i] = '#'
    return plain
  while len(plain) != lowest_point + 2:
    plain.append(['.' for _ in range(len(plain[0]))])
  plain.append(['#' for _ in range(len(plain[0]))])
  return plain



if __name__ == "__main__":
  with open("day14/input.txt") as file:
    lines = file.read().strip().split("\n")
    paths = list(map(lambda x: x.split(" -> "), lines))
    coords = []
    for path in paths:
      coord_path = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in path]  
      coords.append(coord_path)

  plain = prepare_map(coords)
  print(simulate_sand(plain, 500))

  plain = plain_with_floor(plain, coords)
  print(simulate_sand(plain, 500, True))

  # amount = 0
  # for row in plain[:15]:
  #   for el in row[485:515]:
  #     print(el,end='')
  #     if el == 'o': amount += 1
  #   print()

  amount = 0
  for row in plain:
    for el in row:
      if el == 'o': amount += 1
  print(amount) #reusing the board from ex. 1, so sum of already existing grains
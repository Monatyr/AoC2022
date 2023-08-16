def check_if_visible(plain, y_val, x_val):
  height = int(plain[y_val][x_val])

  left, right, up, down = False, False, False, False
  for i, el in enumerate(plain[y_val]):
    if int(el) >= height:
      if i < x_val: left = True
      elif i > x_val: right = True

  for i in range(len(plain)):
    if int(plain[i][x_val]) >= height:
      if i < y_val: up = True
      elif i > y_val: down = True
  
  return not left or not right or not up or not down


def calculate_scenic_score(lines, y, x):
  if y == 0 or x == 0 or y == len(lines)-1 or x == len(lines[0])-1:
    return 0
  height = int(lines[y][x])
  score = 1

  trees = 0
  for i in range(x-1, -1, -1):
    trees += 1
    if int(lines[y][i]) >= height:
      break
  score *= trees

  trees = 0
  for i in range(x+1, len(lines[y])):
    trees += 1
    if int(lines[y][i]) >= height:
      break
  score *= trees

  trees = 0
  for i in range(y-1, -1, -1):
    trees += 1
    if int(lines[i][x]) >= height:
      break
  score *= trees

  trees = 0
  for i in range(y+1, len(lines)):
    trees += 1
    if int(lines[i][x]) >= height:
      break
  score *= trees

  return score


def first_excercise(lines):
  visible = (len(lines) + len(lines[0])) * 2 - 4
  for i, line in enumerate(lines):
    if i == 0 or i == len(lines)-1:
      continue
    for j, el in enumerate(line):
      if j == 0 or j == len(line)-1:
        continue
      if(check_if_visible(lines, i, j)):
        visible += 1
  
  return visible


def second_exercise(lines):
  max_value = 0
  for i, line in enumerate(lines):
    for j, el in enumerate(line):
      score = calculate_scenic_score(lines, i, j)
      max_value = max(max_value, score)
  return max_value


if __name__ == "__main__":
  with open("day8/input.txt") as file:
    lines = list(map(str.strip, file.readlines()))
  print(first_excercise(lines))
  print(second_exercise(lines))

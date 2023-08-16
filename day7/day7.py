import time

def time_it(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(time.time() - start)
    return result
  return wrapper


#tree[i] = {dirs: list[str], size: int, checked: bool}

def read_tree(lines):
  tree = {"/": [[], 0, False]}
  curr_dir = "/"
  for line in lines:
    parts = line.split()
    if parts[0] == "$":
      if parts[1] == "cd":
        if parts[2] == "/":
          curr_dir = "/"
        elif parts[2] == "..":
          split_path = list(filter(lambda x: x != '', curr_dir.split("/")))
          curr_dir = "/" + "/".join(split_path[:len(split_path)-1]) + "/"
          if len(curr_dir) == 2:
            curr_dir = "/"
        else:
          curr_dir += parts[2] + "/"
        if not tree.get(curr_dir):
          tree[curr_dir] = [[], 0, False]
      elif parts[1] == "ls":
        pass
    elif parts[0] == "dir":
      tree[curr_dir][0].append(curr_dir + parts[1] + "/")
    else:
      tree[curr_dir] = [tree[curr_dir][0], tree[curr_dir][1] + int(parts[0]), False]
  return tree


def find_size(dir_name, tree):
  if tree[dir_name][2]:
    return tree[dir_name][1]

  for el in tree[dir_name][0]:
    child_size = find_size(el, tree)
    tree[dir_name][1] += child_size

  tree[dir_name][2] = True
  return tree[dir_name][1]

# @time_it
def first_exercise(tree):
  find_size("/", tree)
  result = 0
  for el in tree.values():
    if el[1] <= 100000:
      result += el[1]
  return result


def second_exercise(tree, limit=70000000, unused=30000000):
  occupied = tree["/"][1]
  print("HELLO: ", limit-occupied)
  diff = limit - occupied
  wanted = unused - diff
  print("WANTED: ", wanted)
  return min(list(filter(lambda x: x[1] > wanted, tree.values())), key=lambda x: x[1])[1]


if __name__ == "__main__":
  with open("day7/input.txt") as file:
    lines = list(map(str.strip, file.readlines()))

  tree = read_tree(lines)

  result1 = first_exercise(tree)
  result2 = second_exercise(tree)
  print(result1)
  print(result2)


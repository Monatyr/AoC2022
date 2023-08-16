from copy import deepcopy
import sys
sys.setrecursionlimit(30000)

class Valve:
  def __init__(self, index, flow_rate, neighbours):
    self.index = index
    self.flow_rate = flow_rate
    self.neighbours = neighbours


class Path:
  def __init__(self, visited: set[str], steam_released: int, time_left: int, current_node: str):
    self.visited = visited
    self.steam_released = steam_released
    self.time_left = time_left
    self.current_node = current_node


#returns adjacency matrix (-1 - not directly connected, 0 - same node, 1 - directly connected)
def dict_graph_to_adj_matrix(G):
  matrix = [[-1 for _ in range(len(G))] for _ in range(len(G))]
  for node in G.values():
    matrix[node.index][node.index] = 0 
    for neigbhour in node.neighbours:
      matrix[node.index][G[neigbhour].index] = 1
  return matrix


def floyd_warshall(G: list[Valve]): #G as dict of Valve names (tbd if correct form)
  G = dict_graph_to_adj_matrix(G) #transform to adj_matrix
  n = len(G)
  distances = [[float('+inf') if G[i][j] == -1 else G[i][j] for j in range(n)] for i in range(n)]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
  return distances


#get rid of zero flow rate valves in Graph and in neighbours of valves
def simplify_graph(G: dict):
  new_G, non_zero = dict(), []

  for key, value in G.items():
    if value.flow_rate or key == 'AA': non_zero.append(key)
  for key, value in G.items():
    if key in non_zero:
      new_G[key] = Valve(value.index, value.flow_rate, list(filter(lambda x: x in non_zero, value.neighbours)))
  return new_G


def time_to_open_valve(distances, s: int, t: int):
  return distances[s][t] + 1


def prune_all(G: dict[str, Valve], distances, paths: list[Path]):
  result = []
  if not paths: #first function call
    print("NOT")
    new_paths = []
    for target in G.keys():
      if target != 'AA':
        new_paths.append(Path({'AA'}, 0, 30-time_to_open_valve(distances, G['AA'].index, G[target].index), target))
        el = new_paths[-1]
        # print(el.visited, el.steam_released, el.time_left, el.current_node)
    return prune_all(G, distances, new_paths)

  for path in paths:
    to_visit = set(G.keys()).difference(path.visited)
    new_paths = []
    
    for target in to_visit:
      necessary_time = time_to_open_valve(distances, G[path.current_node].index, G[target].index)
      new_time_left = path.time_left - necessary_time
      if new_time_left <= 0 or G.keys() == path.visited: #or set(G.keys()).difference(path.visited) == {}
        # print(G.keys(), path.visited)
        result.append(path)
        continue #???????????????

      new_visited = deepcopy(path.visited)
      new_visited.add(target)
      new_path = Path(new_visited, path.steam_released + new_time_left * G[target].flow_rate, new_time_left, target)
      new_paths.append(new_path)
    result.extend(prune_all(G, distances, new_paths))
  return result


if __name__ == "__main__":
  with open('day16/input.txt') as file:
    lines = file.read().strip().split("\n")
    G = dict()
    for i, line in enumerate(lines):
      elems = line.split()
      neighbours = list(map(lambda x: x.replace(',', ''), elems[9: len(elems)]))
      G[elems[1]] = Valve(i, int(''.join(el for el in elems[4] if el.isnumeric())), neighbours)

  distances = floyd_warshall(G)
  simple_G = simplify_graph(G)

  paths_1 = prune_all(simple_G, distances, [])
  print(paths_1[0])


  #what's love got to do ;)


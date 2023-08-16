from functools import cmp_to_key

class Valve:
  def __init__(self, index, flow_rate, neighbours):
    self.index = index
    self.flow_rate = flow_rate
    self.neighbours = neighbours


class Path:
  def __init__(self, visited: list(str), steam_released: int):
    self.visited = visited
    self.steam_released = steam_released


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
  

def released_pressure(time_left, flow_rate):
  return time_left * flow_rate


#get not yet open valves sorted by the amount of preasure they will release till the end of time if opened as next step
def sorted_preasure_nodes_from_node(node: Valve, distances: list[list[int]], closed_nodes: list[Valve], time_left: int):
  def sort_by_preasure_production(x1: Valve, x2: Valve):
    d1, d2 = distances[node.index][x1.index], distances[node.index][x2.index]
    p1 = 0 if time_left <= 1 + d1 else (time_left - d1 - 1) * x1.flow_rate
    p2 = 0 if time_left <= 1 + d2 else (time_left - d2 - 1) * x2.flow_rate
    
    return p1 < p2

  return sorted(closed_nodes, key=cmp_to_key(sort_by_preasure_production))



def exercise(G):
  pass



# The idea is to prune all of the solutions using DFS.
# Problem: how to decide that a solution is not worth continuing? On the other hand maybe trying all of the possibilities is not that bad (could be terrible, have not given it much thought :))?
# Probably should eliminate all of the 0 flow valves from the list of nodes. 

# I will try to prune all possible paths. Could be disasterous. We'll see.
def dfs_prunning(graph, distances, time_left, paths):
  



if __name__ == "__main__":
  with open('day16/input.txt') as file:
    lines = file.read().strip().split("\n")
    G = dict()
    for i, line in enumerate(lines):
      elems = line.split()
      neighbours = list(map(lambda x: x.replace(',', ''), elems[9: len(elems)]))
      G[elems[1]] = Valve(i, int(''.join(el for el in elems[4] if el.isnumeric())), neighbours)


  distances = floyd_warshall(G)

  for el in distances:
    print(el)




# Idea 1

# Starting from the current node create a list of steam released by a valve in each node until the end of the 30 minutes given the actual time left.
# So if we are in node A, we use the distance from the Floyd-Warshall algorithm to tell us the number of minutes that we need to spend travelling to a specific node. The time left
# after subtracting those minutes (minus 1 minute needed for opening the valve) is then multiplied by the rate at each the valve is releasing steam. That gives us a sorted list of released
# steam by each node starting from the current one.
# 
# Now the part that I'm unsure about begins, I may later debunk it. We select the top node and begin our journey towards it. If on our way we encounter a node at which it is benefitial
# to stop and open its valve (while keeping in mind the maximum value found previously and how it will adjust with the later released steam by one turn - if it is better to keep moving
# and release ONE more turn of steam in the best valve, then we should not waste our time opening a valve on our way to it. So the amount of steam in the current node multiplied by the time
# left must be greater than one turn of the best node)
# 

# Given more thought the above idea will not work. If we imagine a cave system in the form of a straight line, where the begining node is right in the middle. One side of the system
# can have the best valve right at the end and all of the nodes leading up to it terrible. In contrast the other side might have almost the best but not quite valves all lined up one after
# another. 


# Idea 2

# For each node find a path leading to all of the other nodes with the most benefitial score given the time left. Each next node should be closer to the target node by 1. If there is
# an available detour (same amount of steps to the target node as from the current node or greater by 1) it must be benefitial to take it. So either spend two more turns travelling to the
# target in case of the same distance node (go to node instead of target, open the valve and continue to target) or three more turns ins case of a greater amount of steps (go to node instead
# of target, open the valve, go back to the previous node and continue or go to another node which is either closer or benefitial to the final score)



# Idea 3

# Dynamic programming :) Create a 3D cube instead of a 2D dynamic table. One axis is the current node, the other is the number of currently considered nodes (first 2 / first 3 /  ...and so on)
# and the last one is the current time (from 0 to 29). The value of the cell is the current maximum production (or not current production but total steam released so far (or both)) which can be
# acomplished by being in this node at this time (and considering only the first M nodes).
#
# Iterating over the nubmer of considered nodes would be the most outer loop, then the first inner loop would be the time spent (?) and then the most inner would be the actual nodes.
# Each cell should probably keep more information than just the current production or total steam released but rather a whole data structure with the mentioned values and already open valves in
# such scenario.

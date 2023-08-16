import json

def compare_ints(i1, i2):
  return i1 <= i2


def compare_lists(l1, l2):
  n1, n2, i = len(l1), len(l2), 0

  while i < n1 and i < n2:
    if not compare(l1[i], l2[i]):
      return False
    elif l1[i] == l2[i]:
      i+=1
    else:
      return True
  if i == n2 and i != n1:
    return False
  return True


def compare_list_with_int(el1, el2):
  if type(el1) is not list:
    return compare([el1], el2)
  return compare(el1, [el2])


def compare(el1, el2):
  if type(el1) is list and type(el2) is list:
    return compare_lists(el1, el2)
  if type(el1) is int and type(el2) is int:
    return compare_ints(el1, el2)
  return compare_list_with_int(el1, el2)


def find_correct(pairs):
  result = 0
  for i, pair in enumerate(pairs):
    el1, el2 = json.loads(pair[0]), json.loads(pair[1]) 

    if compare(el1, el2):
      result += i + 1

  return result


def sort_packets(packets):
  n = len(packets)
  swaps = 0

  for i in range(n):
    for j in range(i+1, n):
      if not compare(packets[i], packets[j]):
        packets[i], packets[j] = packets[j], packets[i]
        swaps += 1
  return packets


def find_markers(sorted_packets):
  result = 1
  for i, line in enumerate(sorted_packets):
    str_line = str(line)
    if str_line == '[[2]]' or str_line == '[[6]]':
      print(str_line)
      print(i+1)
      result *= i + 1
  return result
  

if __name__ == "__main__":
  with open("day13/input.txt") as file:
    pairs = file.read().split("\n\n")
    tuple_pairs = [el.split("\n") for el in pairs]
  with open("day13/input.txt") as file:
    packets = list(map(lambda x: json.loads(x), list(filter(lambda x: x != '\n', list(file.readlines())))))
  print(find_correct(tuple_pairs))
  print(find_markers(sort_packets(packets)))


import time

def time_it(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    res = func(*args, **kwargs)
    print("Time:", time.time() - start)
    return res
  return wrapper

def all_different(arr):
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i] == arr[j]: return False
  return True

@time_it
def solution(data: str, offset=4):
  last_four = list(data[:offset])
  
  for i, char in enumerate(data[offset:]):
    if all_different(last_four):
      return i+offset
    last_four.pop(0)
    last_four.append(char)
  return -1


if __name__ == "__main__":
  with open("day6/input.txt") as file:
    lines = file.readlines()[0].strip()

  print(solution(lines))
  print(solution(lines, 14))
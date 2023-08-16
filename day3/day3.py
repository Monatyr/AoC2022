def item_priority(item):
  ascii_value = ord(item)
  return ascii_value - 38 if ascii_value >= 65 and ascii_value <= 90 else ascii_value - 96

def find_same_item(arr1, arr2):
  n = len(arr1)
  
  for i in range(n):
    for j in range(n):
      if arr1[i] == arr2[j]:
        return arr1[i]
  
  return None


def first_excercise():
  priority_sum = 0
  with open("day3/input.txt", 'r') as file:
    lines = file.readlines()
  
  for line in lines:
    n = len(line)
    same_item = find_same_item(line[:n//2], line[n//2:].strip())
    priority_sum += item_priority(same_item)

  return priority_sum


def second_excercise():
  priority_sum = 0
  with open("day3/input.txt", "r") as file:
    lines = file.readlines()
  
  for i in range(0, len(lines), 3):
    two_rucksacks = [{}, {}]

    for j, rucksack in enumerate(two_rucksacks):
      for el in lines[i+j].strip(): rucksack[el] = True

    for el in lines[i+2]:
      if two_rucksacks[0].get(el) and two_rucksacks[1].get(el):
        priority_sum += item_priority(el)
        break
  
  return priority_sum
    

if __name__ == "__main__":
  print(first_excercise())
  print(second_excercise())
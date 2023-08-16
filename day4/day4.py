def both_excercises():
  completely_overlapping, partially_overlapping = 0, 0
  for el in ranges:
    if (int(el[0][0]) - int(el[1][0])) * (int(el[0][1]) - int(el[1][1])) <= 0:
      completely_overlapping += 1
    if (int(el[0][0]) - int(el[1][1])) * (int(el[0][1]) - int(el[1][0])) <= 0:
      partially_overlapping += 1
  return completely_overlapping, partially_overlapping


if __name__ == "__main__":
  with open("day4/input.txt") as file:
    lines = file.readlines()
    ranges = [(el.split(",")[0].split("-"), el.strip().split(",")[1].split("-")) for el in lines]

  print(both_excercises())
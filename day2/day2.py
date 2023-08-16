map_of_duels = {
  "A": {"X": 3, "Y": 6, "Z": 0},
  "B": {"X": 0, "Y": 3, "Z": 6},
  "C": {"X": 6, "Y": 0, "Z": 3}
}
map_of_strategy = {
  "A": {"X": "Z", "Y": "X", "Z": "Y"},
  "B": {"X": "X", "Y": "Y", "Z": "Z"},
  "C": {"X": "Y", "Y": "Z", "Z": "X"}
}
map_of_strength = {"X": 1, "Y": 2, "Z": 3}
map_of_points = {"X": 0, "Y": 3, "Z": 6}


def first_exercise():
  with open("input.txt", "r") as file:
    lines = file.readlines()
  score = 0
  for line in lines:
    score += map_of_strength[line[2]] + map_of_duels[line[0]][line[2]]
  return score


def second_excercise():
  with open("input.txt", "r") as file:
    lines = file.readlines()
  score = 0
  for line in lines:
    what_to_play = map_of_strategy[line[0]][line[2]]
    score += map_of_points[line[2]] + map_of_strength[what_to_play]
  return score

if __name__ == "__main__":
  print(first_exercise())
  print(second_excercise())
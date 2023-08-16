def top_elf():
  max_calories = 0
  curr_sum = 0
  with open("input.txt", 'r') as file:
    lines = file.readlines()
    
    for line in lines:
      if line == "\n":
        max_calories = max(curr_sum, max_calories)
        curr_sum = 0
      else:
        curr_sum += int(line)
      
  return max_calories


def top_three_elves():
  first_place, second_place, third_place = 0, 0, 0
  curr_sum = 0
  with open("input.txt", 'r') as file:
    lines = file.readlines()
    
    for line in lines:
      if line == "\n":
        if curr_sum >= first_place:
          third_place = second_place
          second_place = first_place
          first_place = curr_sum
        elif curr_sum >= second_place:
          third_place = second_place
          second_place = curr_sum
        elif curr_sum >= third_place:
          third_place = curr_sum
        curr_sum = 0
      else:
        curr_sum += int(line)
      
  return first_place + second_place + third_place


if __name__ == "__main__":
  print(top_elf())
  print(top_three_elves())
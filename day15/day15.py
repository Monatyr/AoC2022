class Sensor:
  def __init__(self, pos, beacon):
    self.pos = pos
    self.beacon = beacon


def manhattan_distance(t1, t2):
  return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])


def get_covered_in_row(sensor: Sensor, target_row):
  manh_dist = manhattan_distance(sensor.pos, sensor.beacon)
  height_diff = abs(sensor.pos[0] - target_row)
  tiles_number = 2 * manh_dist + 1 - 2 * height_diff
  return set([(target_row, el) for el in range(sensor.pos[1] - tiles_number//2, sensor.pos[1] + tiles_number//2 + 1)])


def first_exercise(sensors: list[Sensor], target_row=2000000):
  occupied, beacons_in_target_row = set(), set()
  for sensor in sensors:
    height_diff = manhattan_distance(sensor.pos, sensor.beacon)
    if sensor.pos[0] - height_diff > target_row or sensor.pos[0] + height_diff < target_row:
      continue
    if sensor.beacon[0] == target_row:
      beacons_in_target_row.update([sensor.beacon[1]])
    occupied_tiles = get_covered_in_row(sensor, target_row)
    occupied.update(occupied_tiles)
  return len(occupied) - len(beacons_in_target_row)


def find_gap(ranges):
  left_range = min(ranges, key=lambda x: x[0])
  return left_range[1] + 1


def get_row_range_for_sensor(sensor: Sensor, row_index):
  max_range = manhattan_distance(sensor.pos, sensor.beacon)
  sensor_y = sensor.pos[0]
  height_diff = abs(sensor_y - row_index)
  if sensor_y - max_range <= row_index and sensor_y + max_range >= row_index:
    return [sensor.pos[1] - max_range + height_diff, sensor.pos[1] + max_range - height_diff] 
  return []


def merge_ranges(ranges, sensor_range):
  if not ranges:
    return [sensor_range] if sensor_range else []
  if not sensor_range:
    return ranges
  
  ranges.append(sensor_range)
  ranges.sort(key=lambda x: x[0])
  res_ranges = []
  curr_range = ranges[0]

  for i in range(1, len(ranges)):
    if curr_range[0] <= ranges[i][1] and curr_range[1] >= ranges[i][0]:
      curr_range = [min(curr_range[0], ranges[i][0]), max(curr_range[1], ranges[i][1])]
    else:
      res_ranges.append(curr_range)
      curr_range = ranges[i]
    if i == len(ranges) - 1:
        res_ranges.append(curr_range)
  if not res_ranges:
    return [curr_range]
  return res_ranges


def second_exercise(sensors: list[Sensor], range_limit: int=4000000):
  ranges = [[] for _ in range(range_limit+1)]
  for i in range(range_limit+1):
    for sensor in sensors:
      sensor_range = get_row_range_for_sensor(sensor, i)
      ranges[i] = merge_ranges(ranges[i], sensor_range)
    if len(ranges[i]) > 1:
      print(ranges[i], i)
      gap_x = find_gap(ranges[i])
      return gap_x * range_limit + i
  return None


if __name__ == "__main__":
  with open("day15/input.txt") as file:
    lines = file.read().strip().split("\n")
    sensors = []
    for line in lines:
      line = line.split()
      temp_data = (line[2], line[3], line[8], line[9])
      data = []
      for el in temp_data:
        data.append(int(el[2:].replace(',', '').replace( ':', '')))
      sensors.append(Sensor((data[1], data[0]), (data[3], data[2])))
  print(second_exercise(sensors))
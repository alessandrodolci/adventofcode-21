import os


class Point:
  x: int
  y: int

  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
      return '(' + str(self.x) + ',' + str(self.y) + ')'


class VentLine:
  start: Point
  end: Point

  def __init__(self, start: Point, end: Point) -> None:
    self.start = start
    self.end = end

  def __str__(self) -> str:
      return str(self.start) + ' -> ' + str(self.end)


def mark_vent_lines_on_grid(grid: 'list[list[int]]', vent_lines: 'list[VentLine]'):
  for vent_line in vent_lines:
    if vent_line.start.x != vent_line.end.x and vent_line.start.y != vent_line.end.y:
      distance = abs(vent_line.end.x - vent_line.start.x)

      if vent_line.start.x < vent_line.end.x and vent_line.start.y < vent_line.end.y:
        for i in range(distance + 1):
          grid[vent_line.start.x + i][vent_line.start.y + i] += 1
      elif vent_line.start.x < vent_line.end.x and vent_line.start.y > vent_line.end.y:
        for i in range(distance + 1):
          grid[vent_line.start.x + i][vent_line.start.y - i] += 1
      elif vent_line.start.x > vent_line.end.x and vent_line.start.y < vent_line.end.y:
        for i in range(distance + 1):
          grid[vent_line.start.x - i][vent_line.start.y + i] += 1
      else:
        for i in range(distance + 1):
          grid[vent_line.start.x - i][vent_line.start.y - i] += 1

      continue

    for i in range(min(vent_line.start.x, vent_line.end.x), max(vent_line.start.x, vent_line.end.x)+1):
      for j in range(min(vent_line.start.y, vent_line.end.y), max(vent_line.start.y, vent_line.end.y)+1):
        grid[i][j] += 1


def get_points_with_overlapping_lines(grid: 'list[list[int]]'):
  result = 0
  for line in grid:
    result += sum(x >= 2 for x in line)

  return result


vent_lines: 'list[VentLine]' = []
with open(os.path.join('input', 'input.txt'), 'r') as input_file:
  lines = [line.strip() for line in input_file.readlines()]
  for line in lines:
    tokens = line.split(' -> ')

    start_coordinates = tokens[0].split(',')
    start = Point(int(start_coordinates[0]), int(start_coordinates[1]))

    end_coordinates = tokens[1].split(',')
    end = Point(int(end_coordinates[0]), int(end_coordinates[1]))

    vent_lines.append(VentLine(start, end))


horizontal_length = 0
vertical_length = 0
for vent_line in vent_lines:
  horizontal_length = max(horizontal_length, max(
      vent_line.start.x, vent_line.end.x))
  vertical_length = max(vertical_length, max(
      vent_line.start.y, vent_line.end.y))

grid = []
for i in range(horizontal_length+1):
  line = []
  for j in range(vertical_length+1):
    line.append(0)
  grid.append(line)

mark_vent_lines_on_grid(grid, vent_lines)

result = get_points_with_overlapping_lines(grid)

print('The number of points with at least two overlapping lines is: ' + str(result))

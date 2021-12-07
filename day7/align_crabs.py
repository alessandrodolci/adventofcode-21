from collections import defaultdict
import math
import os


def get_best_position_fuel(crabs_on_positions: 'dict[int, int]'):
  result = math.inf

  for position in crabs_on_positions:
    total_fuel_needed = 0
    for initial_position in crabs_on_positions:
      if initial_position != position:
        # expensive and inefficient
        fuel_needed = sum(
            [x for x in range(1, abs(position - initial_position) + 1)])
        total_fuel_needed += fuel_needed * crabs_on_positions[initial_position]
    if total_fuel_needed < result:
      result = total_fuel_needed

  return result


positions: 'list[int]' = []
with open(os.path.join('input', 'input.txt'), 'r') as input_file:
  positions = [int(position)
               for position in input_file.readline().strip().split(',')]

crabs_on_positions: 'dict[int, int]' = defaultdict(lambda: 0)
for position in positions:
  crabs_on_positions[position] += 1

result = get_best_position_fuel(crabs_on_positions)

print('The fuel needed to align at the best position available is: ' + str(result))

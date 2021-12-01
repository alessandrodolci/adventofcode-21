import os


def get_single_measurements_increases(measurements):
  result = 0
  current_measurement = None

  for next_measurement in measurements:
    if current_measurement != None and next_measurement > current_measurement:
      result += 1

    current_measurement = next_measurement

  return result


def get_sliding_windows_measurements_increases(measurements):
  result = 0
  current_measurements = [None, None, None, None]

  for next_measurement in measurements:
    current_measurements.pop(0)
    current_measurements.append(next_measurement)
    if None not in current_measurements:
      first_window = sum(current_measurements[0:3])
      second_window = sum(current_measurements[1:4])
      if (second_window > first_window):
        result += 1

  return result


lines = []
with open(os.path.join('input', 'input.txt'), 'r') as input_file:
  lines = [line.strip() for line in input_file.readlines()]

measurements = [int(line) for line in lines]
result = get_sliding_windows_measurements_increases(measurements)

print("The number of measurements which are larger than the previous is: ", result)

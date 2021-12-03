import os

ZERO = '0'
ONE = '1'


def get_most_common_bit(numbers, index):
  zero_count = 0
  one_count = 0
  for number in numbers:
    if number[index] == '0':
      zero_count += 1
    elif number[index] == '1':
      one_count += 1
    else:
      raise ValueError(number[index])

  if zero_count > one_count:
    return ZERO
  elif zero_count < one_count:
    return ONE
  else:
    return None


def get_power_consumption(numbers: list):
  numbers_length = len(numbers[0])

  gamma_rate_digits = []
  epsilon_rate_digits = []
  for i in range(numbers_length):
    most_common_bit = get_most_common_bit(numbers, i)

    if (most_common_bit == None):
      raise ValueError(most_common_bit)
    least_common_bit = '1' if most_common_bit == ZERO else '0'

    gamma_rate_digits.append(most_common_bit)
    epsilon_rate_digits.append(least_common_bit)

  gamma_rate = int(''.join(gamma_rate_digits), 2)
  epsilon_rate = int(''.join(epsilon_rate_digits), 2)

  return gamma_rate * epsilon_rate


def get_life_support_rating(numbers: list):
  numbers_length = len(numbers[0])

  og_rating_numbers = numbers.copy()
  for i in range(numbers_length):
    most_common_bit = get_most_common_bit(og_rating_numbers, i)

    if len(og_rating_numbers) > 1:
      og_bit = '1' if most_common_bit == ONE or most_common_bit == None else '0'
      og_rating_numbers = [
          number for number in og_rating_numbers if number[i] == og_bit]
    else:
      break

  cs_rating_numbers = numbers.copy()
  for i in range(numbers_length):
    most_common_bit = get_most_common_bit(cs_rating_numbers, i)

    if len(cs_rating_numbers) > 1:
      cs_bit = '0' if most_common_bit == ONE or most_common_bit == None else '1'
      cs_rating_numbers = [
          number for number in cs_rating_numbers if number[i] == cs_bit]
    else:
      break

  og_rating = int(''.join(og_rating_numbers[0]), 2)
  cs_rating = int(''.join(cs_rating_numbers[0]), 2)

  return og_rating * cs_rating


lines = []
with open(os.path.join('input', 'input.txt'), 'r') as input_file:
  lines = [line.strip() for line in input_file.readlines()]

result = get_life_support_rating(lines)
print('The life support rating is: ' + str(result))

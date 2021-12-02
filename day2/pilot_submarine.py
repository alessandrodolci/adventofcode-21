import os


def get_final_coordinates_product_with_wrong_rules(lines):
    horizontal_position = 0
    depth = 0
    for line in lines:
        tokens = line.split()
        command = tokens[0]
        value = int(tokens[1])

        if command == 'forward':
            horizontal_position += value
        elif command == 'up':
            depth -= value
        elif command == 'down':
            depth += value
        else:
            raise ValueError(command)

    return horizontal_position * depth


def get_final_coordinates_product_with_correct_rules(lines):
    horizontal_position = 0
    depth = 0
    aim = 0
    for line in lines:
        tokens = line.split()
        command = tokens[0]
        value = int(tokens[1])

        if command == 'forward':
            horizontal_position += value
            depth += aim * value
        elif command == 'up':
            aim -= value
        elif command == 'down':
            aim += value
        else:
            raise ValueError(command)

    return horizontal_position * depth


lines = []
with open(os.path.join('input', 'input.txt'), 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

result = get_final_coordinates_product_with_correct_rules(lines)

print('The product of the final horizontal position and depth is: ' + str(result))

import os


def get_board_score(board: list, last_drawn_number: str):
    unmarked_numbers = []
    for line in board:
        unmarked_numbers.extend([int(number)
                                 for number in line if number != 'x'])

    return sum(unmarked_numbers) * int(last_drawn_number)


def check_for_winning_boards(boards: list):
  for board_index, board in enumerate(boards):
    for i in range(5):
      winning_row = True
      for j in range(5):
        if board[i][j] != 'x':
          winning_row = False
      if winning_row:
        return (board, board_index)

    for j in range(5):
      winning_column = True
      for i in range(5):
        if board[i][j] != 'x':
          winning_column = False
      if winning_column:
        return (board, board_index)

  return None


def get_first_winning_board_score(boards: list, drawn_numbers: str):
  for drawn_number in drawn_numbers:
    for board in boards:
      for line in board:
        if drawn_number in line:
          line[line.index(drawn_number)] = 'x'

    winning_board = check_for_winning_boards(boards)
    if winning_board:
      return get_board_score(winning_board[0], drawn_number)


def get_last_winning_board_score(boards: list, drawn_numbers: str):
  for drawn_number in drawn_numbers:
    for board in boards:
      for line in board:
        if drawn_number in line:
          line[line.index(drawn_number)] = 'x'

    winning_board = check_for_winning_boards(boards)
    while winning_board:
      if len(boards) > 1:
        boards.pop(winning_board[1])
      else:
        return get_board_score(winning_board[0], drawn_number)

      winning_board = check_for_winning_boards(boards)


drawn_numbers = []
boards = []
with open(os.path.join('input', 'input.txt'), 'r') as input_file:
  drawn_numbers = input_file.readline().strip().split(',')
  current_board = []
  for line in [line.strip() for line in input_file.readlines() if line.strip()]:
    if len(current_board) < 4:
      current_board.append(line.split())
    else:
      current_board.append(line.split())
      boards.append(current_board)
      current_board = []

result = get_last_winning_board_score(boards, drawn_numbers)

print('The score of the last winning board is: ' + str(result))

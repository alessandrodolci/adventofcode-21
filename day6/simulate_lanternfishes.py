import os

DAYS = 256

def get_fishes_after_simulation(fishes_by_days: 'dict[int, int]'):
    for i in range(DAYS):
        newborn_count = fishes_by_days[0]
        for j in range(8):
            fishes_by_days[j] = fishes_by_days[j+1]
        fishes_by_days[6] += newborn_count
        fishes_by_days[8] = newborn_count

    return sum(fishes_by_days.values())

fishes_days = []
with open(os.path.join('input', 'input.txt'), 'r') as input_file:
    fishes_days = [int(counter) for counter in input_file.readline().strip().split(',')]

fishes_by_days = {}
for i in range(9):
    fishes_by_days[i] = 0

for fish_days in fishes_days:
    fishes_by_days[fish_days] += 1

result = get_fishes_after_simulation(fishes_by_days)

print('The number of lanternfishes after ' + str(DAYS) + ' days is: ' + str(result))

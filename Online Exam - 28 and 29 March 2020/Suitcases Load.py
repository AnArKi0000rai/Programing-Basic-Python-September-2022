trunk_capacity = float(input())
capacity_available = trunk_capacity
count_suitcase = 0
command = input()
while command != "End":
    suitcase_volume = float(command)
    count_suitcase += 1
    if count_suitcase % 3 != 0:
        capacity_available -= suitcase_volume
    else:
        capacity_available -= suitcase_volume + (suitcase_volume * 0.10)

    if capacity_available <= 0:
        count_suitcase -= 1
        break

    command = input()

if capacity_available >= 0:
    print('Congratulations! All suitcases are loaded!')
    print(f'Statistic: {count_suitcase} suitcases loaded.')
else:
    print('No more space!')
    print(f'Statistic: {count_suitcase} suitcases loaded.')




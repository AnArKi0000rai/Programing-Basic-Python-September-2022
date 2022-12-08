count_bottles = int(input())

liquid_volume = count_bottles * 750
wash_cycle = 0
pots = 0
plates = 0

line_input = input()
while line_input != 'End':
    current_data = int(line_input)
    wash_cycle += 1
    if wash_cycle == 3:
        liquid_volume -= (current_data * 15)
        pots += current_data
        wash_cycle = 0
    else:
        liquid_volume -= (current_data * 5)
        plates += current_data
    if liquid_volume < 0:
        break

    line_input = input()
diff = abs(liquid_volume)
if liquid_volume < 0:
    print(f'Not enough detergent, {diff} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {diff} ml.')



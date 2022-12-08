length = int(input())
width = int(input())
high = int(input())

whole_space = length * width * high

data_input = input()
while data_input != 'Done':
    current_data = int(data_input)
    whole_space -= current_data
    if whole_space <= 0:
        break

    data_input = input()

space_volume_left = abs(whole_space)

if data_input == 'Done':
    print(f'{space_volume_left} Cubic meters left.')
else:
    print(f'No more free space! You need {space_volume_left} Cubic meters more.')
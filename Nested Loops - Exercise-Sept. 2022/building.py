floors = int(input())
flats = int(input())
flat_type = ''
for floor in range(floors, 0, -1):
    for flat in range(flats):
        flat_number = f'{floor}{flat}'

        if floor == floors:
            flat_type = f'L{flat_number}'
        elif floor % 2 == 0:
            flat_type = f'O{flat_number}'
        else:
            flat_type = f'A{flat_number}'

        print(flat_type, end=' ')
    print()

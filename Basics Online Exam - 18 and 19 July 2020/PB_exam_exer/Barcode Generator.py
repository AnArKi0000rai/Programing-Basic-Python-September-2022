first_number = input()
second_number = input()

for thousands in range(int(first_number[0]), int(second_number[0]) + 1):
    for hundred in range(int(first_number[1]), int(second_number[1]) + 1):
        for ten in range(int(first_number[2]), int(second_number[2]) + 1):
            for one in range(int(first_number[3]), int(second_number[3]) + 1):
                if thousands % 2 != 0 and hundred % 2 != 0 and ten % 2 != 0 and one % 2 != 0:
                    print(f'{thousands}{hundred}{ten}{one}', end=' ')







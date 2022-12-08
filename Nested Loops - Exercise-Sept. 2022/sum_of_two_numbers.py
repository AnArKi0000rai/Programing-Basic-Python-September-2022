start_number = int(input())
end_number = int(input())
magic_number = int(input())

combination_counter = 0
flag = False
for a in range(start_number, end_number + 1):
    for b in range(start_number, end_number + 1):
        combination_counter += 1
        current_sum = a + b

        if current_sum == magic_number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f"Combination N:{combination_counter} ({a} + {b} = {magic_number})")
else:
    print(f'{combination_counter} combinations - neither equals {magic_number}')

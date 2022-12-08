number = int(input())

current_numbers = 1
current_bigger_than_n = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current_numbers > number:
            current_bigger_than_n = True
            break
        print(str(current_numbers)+' ', end='')
        current_numbers += 1
        if current_bigger_than_n:
            break
    print()




















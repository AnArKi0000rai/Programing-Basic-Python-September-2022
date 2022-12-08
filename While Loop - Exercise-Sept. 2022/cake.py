length = int(input())
width = int(input())

whole_cake_size = length * width

line_input = input()
while line_input != 'STOP':
    current_input = int(line_input)
    whole_cake_size -= current_input
    if whole_cake_size <= 0:
        break

    line_input = input()
diff = abs(whole_cake_size)

if line_input == 'STOP':
    print(f'{diff} pieces are left.')
else:
    print(f'No more cake left! You need {diff} pieces more.')



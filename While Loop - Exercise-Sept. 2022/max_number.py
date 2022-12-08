import sys

number_max = -sys.maxsize

while True:
    current_num = input()
    if current_num == 'Stop':
        break
    current_num = int(current_num)

    if current_num > number_max:
        number_max = current_num

print(number_max)









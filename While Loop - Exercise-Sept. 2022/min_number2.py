import sys

number_min = sys.maxsize

while True:
    current_num = input()
    if current_num == 'Stop':
        break
    current_num = int(current_num)
    if current_num < number_min:
        number_min = current_num

print(number_min)
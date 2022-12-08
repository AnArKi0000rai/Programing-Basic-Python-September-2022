import sys

current_number = input()

number_max = -sys.maxsize

while current_number != 'Stop':
    current_number = int(current_number)
    if current_number > number_max:
        number_max = current_number
    current_number = input()

print(number_max)

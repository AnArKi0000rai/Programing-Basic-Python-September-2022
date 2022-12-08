import sys

number = input()

number_min = sys.maxsize

while number != 'Stop':
    number = int(number)
    if number < number_min:
        number_min = number
    number = input()

print(number_min)
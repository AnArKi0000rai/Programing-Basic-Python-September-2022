number_of_lines = int(input())

left_numbers = 0
right_numbers = 0

for i in range(2 * number_of_lines):
    current_number = int(input())
    if i < number_of_lines:
        left_numbers += current_number
    elif i >= number_of_lines:
        right_numbers += current_number

if left_numbers == right_numbers:
    print(f'Yes, sum = {left_numbers}')
else:
    diff = abs(left_numbers - right_numbers)
    print(f'No, diff = {diff}')


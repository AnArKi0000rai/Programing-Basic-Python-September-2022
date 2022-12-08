import sys

number_of_lines = int(input())

num_maxsize = -sys.maxsize
number_sum = 0
total_sum = 0

for i in range(1, number_of_lines + 1):
    current_number = int(input())
    if current_number > num_maxsize:
        num_maxsize = current_number

    total_sum += current_number

other_num_sum = total_sum - num_maxsize

if other_num_sum == num_maxsize:
    print('Yes')
    print(f'Sum = {other_num_sum}')
else:
    diff = abs(other_num_sum - num_maxsize)
    print('No')
    print(f'Diff = {diff}')



number_lines = int(input())

evan_sum = 0
odd_sum  = 0

for i in range (1, number_lines + 1):
    current_num = int(input())
    if i % 2 == 0:
        evan_sum += current_num
    else:
        odd_sum += current_num

if evan_sum == odd_sum:
    print('Yes')
    print(f'Sum = {evan_sum}')
else:
    diff = abs(evan_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')

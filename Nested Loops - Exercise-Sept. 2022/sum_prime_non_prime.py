sum_prime = 0
sum_non_prime = 0
data_input = input()

while data_input != 'stop':
    current_data = int(data_input)
    if current_data < 0:
        print("Number is negative.")
        data_input = input()
        continue

    count = 0

    for n in range(1, current_data + 1):
        if current_data % n == 0:
            count += 1

    if count == 2:
        sum_prime += current_data
    else:
        sum_non_prime += current_data

    data_input = input()
print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
number = int(input())

numbers_count = 0
while True:
    numbers_sum = int(input())
    numbers_count += numbers_sum
    if numbers_count >= number:
        print(numbers_count)
        break

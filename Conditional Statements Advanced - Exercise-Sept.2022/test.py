projection_type = input()
rows = int(input())
columns = int(input())

cinema_capacity = rows * columns

price = 0
if projection_type == 'Premiere':
    price = cinema_capacity * 12
elif projection_type == 'Normal':
    price = cinema_capacity * 7.50
elif projection_type == 'Discount':
    price = cinema_capacity * 5


print(f'{price:.2f} leva')
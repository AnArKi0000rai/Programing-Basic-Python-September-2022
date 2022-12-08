age = int(input())
wash_machine_price = float(input())
toy_price = int(input())


birth_day_money = 0
toy_money = 0
additional_lilis_money = 10
birth_day_count = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toy_money += toy_price
    else:
        birth_day_count += 1
        birth_day_money += additional_lilis_money
        additional_lilis_money = additional_lilis_money + 10


total_sum = (birth_day_money + toy_money) - birth_day_count
diff = abs(total_sum - wash_machine_price)

if total_sum >= wash_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
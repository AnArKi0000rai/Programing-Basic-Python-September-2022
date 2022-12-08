price_kilogram_of_vegetables = float(input())
price_kilogram_of_fruit = float(input())
total_kilogram_of_vegetables = int(input())
total_kilogram_of_fruit = int(input())

total_price_of_vegetables = total_kilogram_of_vegetables * price_kilogram_of_vegetables
total_price_of_fruits = total_kilogram_of_fruit * price_kilogram_of_fruit

total_order = total_price_of_vegetables + total_price_of_fruits
price_per_euro = 1.94
total_order_price = total_order / price_per_euro

print(f'{total_order_price:.2f}')

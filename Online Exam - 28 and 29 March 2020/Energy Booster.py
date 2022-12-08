fruit = input()
package_type = input()
numbers_of_package_order = int(input())

price = 0
if fruit == 'Watermelon':
    if package_type == 'small':
        price = 2 * 56
    elif package_type == 'big':
        price = 5 * 28.70
elif fruit == 'Mango':
    if package_type == 'small':
        price = 2 * 36.66
    elif package_type == 'big':
        price = 5 * 19.60
elif fruit == 'Pineapple':
    if package_type == 'small':
        price = 2 * 42.10
    elif package_type == 'big':
        price = 5 * 24.80
elif fruit == 'Raspberry':
    if package_type == 'small':
        price = 2 * 20
    elif package_type == 'big':
        price = 5 * 15.20

total_sum = numbers_of_package_order * price

if 400 <= total_sum <= 1000:
    total_sum -= total_sum * 15 / 100
elif total_sum > 1000:
    total_sum = total_sum / 2

print(f'{total_sum:.2f} lv.')
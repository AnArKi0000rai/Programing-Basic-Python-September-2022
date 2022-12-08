kind_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

price = 0
discount = 0

if kind_of_flowers == 'Roses':
    price = number_of_flowers * 5
    if number_of_flowers > 80:
        discount = price * 0.10
        price = price - discount
elif kind_of_flowers == 'Dahlias':
    price = number_of_flowers * 3.80
    if number_of_flowers > 90:
        discount = price * 0.15
        price = price - discount
elif kind_of_flowers == "Tulips":
    price = number_of_flowers * 2.80
    if number_of_flowers > 80:
        discount = price * 0.15
        price = price - discount
elif kind_of_flowers == "Narcissus":
    price = number_of_flowers * 3
    if number_of_flowers < 120:
        discount = price * 0.15
        price = price + discount
elif kind_of_flowers == "Gladiolus":
    price = number_of_flowers * 2.50
    if number_of_flowers < 80:
        discount = price * 0.20
        price = price + discount

if budget >= price:
    print(f'Hey, you have a great garden with {number_of_flowers} {kind_of_flowers} and {budget-price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')
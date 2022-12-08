budget = int(input())
season = input()
fishers_number = int(input())

boat_price = 0

if season in ("Summer", "Autumn"):
    boat_price = 4200
elif season == 'Spring':
    boat_price = 3000
elif season == 'Winter':
    boat_price = 2600

if fishers_number <= 6:
    boat_price = boat_price * 0.90
elif 6 < fishers_number <= 11:
    boat_price = boat_price * 0.85
elif fishers_number > 11:
    boat_price = boat_price * 0.75

if fishers_number % 2 == 0 and season != 'Autumn':
    boat_price = boat_price * 0.95

total_price = abs(budget - boat_price)

if budget >= boat_price:
    print(f'Yes! You have {total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price:.2f} leva.')




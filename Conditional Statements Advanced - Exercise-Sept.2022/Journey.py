budget = float(input())
season = input()

percent = 0
location = ''
place = ''

if budget <= 100:
    location = "Bulgaria"
    if season == 'summer':
        percent = budget * 0.70
    elif season == 'winter':
        percent = budget * 0.30
elif budget <= 1000:
    location = 'Balkans'
    if season == 'summer':
        percent = budget * 0.60
    elif season == 'winter':
        percent = budget * 0.20
elif budget > 1000:
    location = "Europe"
    percent = budget * 0.10

if season == "summer":
    place = 'Camp'
elif season == 'winter':
    place = 'Hotel'

if location == 'Europe':
    place = 'Hotel'

diff = abs(budget-percent)

print(f'Somewhere in {location}')
print(f'{place} - {diff:.2f}')




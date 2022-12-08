celsius = int(input())
time_of_day = input()

outfit = ""
shoes = ""

if time_of_day == "Morning" and 10 <= celsius <= 18:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
elif time_of_day == 'Afternoon':
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif time_of_day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'


if time_of_day == "Morning" and 18 < celsius <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif time_of_day == 'Afternoon' and 18 < celsius <= 24:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif time_of_day == 'Evening' and 18 < celsius <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'


if time_of_day == "Morning" and celsius >= 25:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif time_of_day == 'Afternoon' and celsius >= 25:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
elif time_of_day == 'Evening' and celsius >= 25:
    outfit = 'Shirt'
    shoes = 'Moccasins'

print(f"It's {celsius} degrees, get your {outfit} and {shoes}.")
the_price_of_luggage_over_20_kg = float(input())
kilograms_of_baggage = float(input())
days_until_the_trip = int(input())
number_of_bags = int(input())

price = 0
if kilograms_of_baggage < 10:
    price = the_price_of_luggage_over_20_kg * 20 / 100
elif 10 <= kilograms_of_baggage <= 20:
    price = the_price_of_luggage_over_20_kg * 0.50
elif kilograms_of_baggage > 20:
    price = the_price_of_luggage_over_20_kg

if days_until_the_trip > 30:
    diff = price * 10 / 100
    price += diff
elif 7 <= days_until_the_trip <= 30:
    diff = price * 15 / 100
    price += diff
elif days_until_the_trip < 7:
    diff = price * 40 / 100
    price += diff

total_sum = price * number_of_bags

print(f'The total price of bags is: {total_sum:.2f} lv.')

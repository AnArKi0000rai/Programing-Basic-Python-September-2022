month = input()
night_numbers = int(input())

apartment_price = 0
studio_price = 0
if month in ('May', 'October'):
    studio_price = night_numbers * 50
    apartment_price = night_numbers * 65
    if 7 < night_numbers <= 14:
        studio_price = studio_price * 0.95
    elif night_numbers > 14:
        studio_price = studio_price * 0.70
        if night_numbers > 14:
            apartment_price = apartment_price * 0.90
elif month in ('June', 'September'):
    studio_price = night_numbers * 75.20
    apartment_price = night_numbers * 68.70
    if night_numbers > 14:
        studio_price = studio_price * 0.80
        if night_numbers > 14:
            apartment_price = apartment_price * 0.90
elif month in ('July', 'August'):
    studio_price = night_numbers * 76
    apartment_price = night_numbers * 77
    if night_numbers > 14:
        apartment_price = apartment_price * 0.90

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
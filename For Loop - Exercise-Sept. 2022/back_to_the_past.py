inherited_money = float(input())
the_year_he_has_to_live_to = int(input())

spend_money = 0
ivans_age = 18

for i in range(1800, the_year_he_has_to_live_to + 1):
    if i > 1800:
        ivans_age += 1
    if i % 2 == 0:
        spend_money += 12000
    else:
        spend_money += 12000 + (ivans_age * 50)


if inherited_money >= spend_money:
    print(f'Yes! He will live a carefree life and will have {inherited_money - spend_money:.2f} dollars left.')
else:
    diff = abs(inherited_money - spend_money)
    print(f'He will need {diff:.2f} dollars to survive.')
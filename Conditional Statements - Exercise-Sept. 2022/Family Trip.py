budget_available = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percentage_for_additional_costs = int(input())

discount_for_more_than_seven_nights = (number_of_nights > 7) * 0.05
annual_discount_per_night = price_per_night * discount_for_more_than_seven_nights
total_discount_per_night = price_per_night - annual_discount_per_night
total_price_per_night = number_of_nights * total_discount_per_night
additional_cost_amount = percentage_for_additional_costs * budget_available / 100

budget_prediction = total_price_per_night + additional_cost_amount
budget_remaining = budget_available - budget_prediction

if budget_remaining >= 0:
    print(f'Ivanovi will be left with {budget_remaining:.2f} leva after vacation.')
elif budget_remaining <= 0:
    print(f'{abs(budget_remaining):.2f} leva needed.')
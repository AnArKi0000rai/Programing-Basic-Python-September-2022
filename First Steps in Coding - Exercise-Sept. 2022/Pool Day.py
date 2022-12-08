import math

number_of_people = int(input())
entrance_fee = float(input())
price_per_sunbed = float(input())
price_for_one_umbrella = float(input())

entrance_fee_event = number_of_people * entrance_fee
sunbed_preferences_provided = number_of_people * 0.75
provided_sunbeds = math.ceil(sunbed_preferences_provided)
annual_sunbed_order = provided_sunbeds * price_per_sunbed
count_umbrella_needed = number_of_people * 0.50
umbrella_order_price = number_of_people - count_umbrella_needed
umbrella_price = math.ceil(umbrella_order_price)* price_for_one_umbrella

total_order_price = entrance_fee_event + annual_sunbed_order + umbrella_price

print(f'{total_order_price:.2f} lv.')

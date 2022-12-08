required_quantities_of_nylon_sq_m = int(input())
required_amount_of_paint_liters = int(input())
amount_of_thinner_liters = int(input())
hours_the_work_will_be_done = int(input())

price_of_nylon_sq_m = (required_quantities_of_nylon_sq_m + 2) * 1.50
additional_paint_liters = required_amount_of_paint_liters * 0.10
paint_price = (required_amount_of_paint_liters + additional_paint_liters) * 14.50
thinner_price = amount_of_thinner_liters * 5.00
price_nylon_bag = 0.40
total_price_consumables = price_of_nylon_sq_m + paint_price + thinner_price \
                          + price_nylon_bag
master_price = (total_price_consumables * 0.30) * hours_the_work_will_be_done

total_order_price = total_price_consumables + master_price

print(total_order_price)
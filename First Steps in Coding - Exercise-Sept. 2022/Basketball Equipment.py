annual_fee_for_basketball_practice = int(input())

annual_price_basketball_fee_per_year = annual_fee_for_basketball_practice
price_for_basketball_shoes = annual_price_basketball_fee_per_year - (annual_fee_for_basketball_practice * 0.40)
cost_basketball_team = price_for_basketball_shoes - (price_for_basketball_shoes * 0.20)
price_of_a_basketball = cost_basketball_team / 4
price_of_basketball_accessories = price_of_a_basketball / 5

total_equipment_cost = annual_price_basketball_fee_per_year + price_for_basketball_shoes \
                       + cost_basketball_team + price_of_a_basketball + price_of_basketball_accessories

print(total_equipment_cost)
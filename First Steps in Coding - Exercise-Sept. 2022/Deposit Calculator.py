deposit_amount = float(input())
deposit_term = int(input())
annual_rate = float(input())

amount_per_year_annual_rate = deposit_amount * (annual_rate / 100)
amount_per_month_annual_rate = amount_per_year_annual_rate / 12
total_amount_per_year = deposit_amount + deposit_term * amount_per_month_annual_rate

print(total_amount_per_year)

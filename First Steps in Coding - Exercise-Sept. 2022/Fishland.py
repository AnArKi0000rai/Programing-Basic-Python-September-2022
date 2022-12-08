kilo_mackerel = float(input())
kilo_sprats = float(input())
kilo_bonito = float(input())
kilo_safrid = float(input())
kilo_mussels = int(input())

per_kilo_bunito = kilo_mackerel + kilo_mackerel * 0.60
price_per_kilo_bunito = kilo_bonito * per_kilo_bunito
per_kilo_safrid = kilo_sprats + kilo_sprats * 0.80
price_per_kilo_safrid = kilo_safrid * per_kilo_safrid
price_per_kilo_mussels = kilo_mussels * 7.50

total_order_price = price_per_kilo_bunito + price_per_kilo_safrid + price_per_kilo_mussels

print(f'{total_order_price:.2f}')



company_name = input()
number_of_adult_ticket = int(input())
kid_ticket_num = int(input())
net_sum_adult_ticket = float(input())
service_fee = float(input())

net_kid_ticket = (net_sum_adult_ticket * 0.30) + service_fee
price_per_adult_ticket_with_service_fee = net_sum_adult_ticket + service_fee

total_price = (number_of_adult_ticket * price_per_adult_ticket_with_service_fee) + (kid_ticket_num * net_kid_ticket)
profit = total_price * 20 / 100
print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')
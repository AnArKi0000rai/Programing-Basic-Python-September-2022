number_of_bitcoins = int(input())
chinese_yuan = float(input())
commission = float(input())

bitcoin_in_lv = 1168
ch_yuan_in_dollar = 0.15
dollar_in_lv = 1.76
euro_in_lv = 1.95

bitcoin_count = number_of_bitcoins * bitcoin_in_lv
count_yuan_in_dollars = chinese_yuan * ch_yuan_in_dollar
dollar_lv = dollar_in_lv * count_yuan_in_dollars

total_sum_in_lv = bitcoin_count + dollar_lv
total_sum_in_eu = total_sum_in_lv / euro_in_lv
commission_sum = total_sum_in_eu * commission / 100
net_sum = total_sum_in_eu - commission_sum

print(f'{net_sum:.2f}')




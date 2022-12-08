city_name = input()
sales_volume = float(input())

trade_commission = 0
flag = True

if city_name == 'Sofia':
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        trade_commission = sales_volume * 0.08
    elif sales_volume > 10000:
        trade_commission = sales_volume * 0.12
    else:
        flag = False

if city_name == 'Varna':
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        trade_commission = sales_volume * 0.10
    elif sales_volume > 10000:
        trade_commission = sales_volume * 0.13
    else:
        flag = False

if city_name == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        trade_commission = sales_volume * 0.12
    elif sales_volume > 10000:
        trade_commission = sales_volume * 0.145

    else:
        flag = False

if flag and trade_commission > 0:
    print(f'{trade_commission:.2f}')
else:
    print('error')
city_name = input()
package_type = input()
vip_client = input()
days_number = int(input())

price = 0
flag = True
if city_name == "Bansko"or city_name == "Borovets":
    if package_type == 'withEquipment':
        price = days_number * 100
        if vip_client == 'yes':
            price = price * 0.90
    elif package_type == 'noEquipment':
        price = days_number * 80
        if vip_client == 'yes':
            price = price * 0.95
        elif vip_client == 'no':
            price = price
        else:
            flag = False
    else:
        flag = False


if city_name == 'Varna' or city_name == 'Burgas':
    if package_type == 'withBreakfast':
        price = days_number * 130
        if vip_client == 'yes':
            price = price * 0.88
    elif package_type == 'noBreakfast':
        price = days_number * 100
        if vip_client == 'yes':
            price = price * 0.93
        elif vip_client == 'no':
            price = price
        else:
            flag = False
    else:
        flag = False


if flag and price > 0:
    print(f'The price is {price:.2f}lv! Have a nice time!')
elif days_number < 1:
    print('Days must be positive number!')
else:
    print('Invalid input!')


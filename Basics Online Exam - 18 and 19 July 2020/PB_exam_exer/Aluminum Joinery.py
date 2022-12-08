number_of_windows = int(input())
type_of_window_frames = input()
shipment_method = input()

price = 0
total_price = 0
flag = False
if type_of_window_frames == '90X130':
    price = 110
    if 30 < number_of_windows <= 60:
        total_price = (number_of_windows * price) * 0.95
    elif number_of_windows > 60:
        total_price = (number_of_windows * price) * 0.92
    else:
        total_price = number_of_windows * price
elif type_of_window_frames == '100X150':
    price = 140
    if 40 < number_of_windows <= 80:
        total_price = (number_of_windows * price) * 0.94
    elif number_of_windows > 80:
        total_price = (number_of_windows * price) * 0.90
    else:
        total_price = number_of_windows * price
elif type_of_window_frames == '130X180':
    price = 190
    if 20 < number_of_windows <= 50:
        total_price = (number_of_windows * price) * 0.93
    elif number_of_windows > 50:
        total_price = (number_of_windows * price) * 0.88
    else:
        total_price = number_of_windows * price
elif type_of_window_frames == '200X300':
    price = 250
    if 25 < number_of_windows <= 50:
        total_price = (number_of_windows * price) * 0.91
    elif number_of_windows > 50:
        total_price = (number_of_windows * price) * 0.86
    else:
        total_price = number_of_windows * price

if shipment_method == 'With delivery':
    total_price += 60

if number_of_windows > 99:
    diff = total_price * 4 / 100
    total_price -= diff

if number_of_windows < 10:
    print('Invalid order')
else:
    print(f'{total_price:.2f} BGN')
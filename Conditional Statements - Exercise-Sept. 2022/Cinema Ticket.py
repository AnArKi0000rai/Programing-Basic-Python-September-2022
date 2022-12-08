weekday = input()

if weekday in ('Monday', 'Tuesday'):
    print('12')
elif weekday in ('Wednesday', 'Thursday'):
    print('14')
elif weekday in ('Saturday', 'Sunday'):
    print('16')
elif weekday == 'Friday':
    print('12')
current_day = input()


if current_day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    print('Working day')
elif current_day in ('Saturday','Sunday'):
    print('Weekend')
else:
    print('Error')
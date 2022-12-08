hour = int(input())
weekday = input()

if 10 <= hour <= 18 and weekday in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
    print('open')
else:
    print('closed')
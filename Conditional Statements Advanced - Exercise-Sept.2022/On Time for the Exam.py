hour_time = int(input())
minute_time = int(input())
hour_arrival_time = int(input())
minute_arrival_time = int(input())

all_exam_time = (hour_time * 60) + minute_time
arrival_time = (hour_arrival_time * 60) + minute_arrival_time
all_minutes = abs(arrival_time - all_exam_time)

if arrival_time > all_exam_time:
    print('Late')
    if all_minutes >= 60:
        hour = all_minutes // 60
        minutes = all_minutes % 60
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{all_minutes} minutes after the start')
elif all_exam_time == arrival_time or all_minutes <= 30:
    print('On time')
    if all_minutes > 0:
        print(f'{all_minutes} minutes before the start')
else:
    print("Early")
    if all_minutes >= 60:
        hour = all_minutes // 60
        minutes = all_minutes % 60
        print(f'{hour}:{minutes:02d} hours before the start ')
    else:
        print(f'{all_minutes} minutes before the start')
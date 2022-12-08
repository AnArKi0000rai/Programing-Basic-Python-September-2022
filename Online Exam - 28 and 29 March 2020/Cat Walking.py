walking_minutes_per_day = int(input())
number_of_daily_walks = int(input())
calories_taken_per_day = int(input())

total_walking_minutes = walking_minutes_per_day * number_of_daily_walks
total_burned_calories = total_walking_minutes * 5
fifty_percent_from_taken_calories = calories_taken_per_day / 2

if total_burned_calories >= fifty_percent_from_taken_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.')
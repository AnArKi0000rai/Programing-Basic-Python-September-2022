number_of_tournaments = int(input())
init_points = int(input())

points = 0
count_wins = 0

for i in range(1, number_of_tournaments + 1):
    tournament_stage = input()
    if tournament_stage == 'W':
        points += 2000
        count_wins += 1
    elif tournament_stage == 'F':
        points += 1200
    elif tournament_stage == 'SF':
        points += 720

total_points = init_points + points
average_points_earned = points / number_of_tournaments
percent_of_wins  = (count_wins / number_of_tournaments) * 100

print(f'Final points: {total_points}')
print(f'Average points: {int(average_points_earned)}')
print(f'{percent_of_wins:.2f}%')
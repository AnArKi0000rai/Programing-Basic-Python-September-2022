actor_name = input()
academy_points = float(input())
number_of_assessors = int(input())

count_points = academy_points

for i in range(1, number_of_assessors + 1):
    assessors_name = input()
    assessors_points = float(input())

    current_points = (len(assessors_name) * assessors_points) / 2
    count_points += current_points
    if count_points >= 1250.5:
        break

if count_points < 1250.5:
    diff = 1250.5 - count_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
else:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {count_points:.1f}!')


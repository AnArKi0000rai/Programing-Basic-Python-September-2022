import sys

max_score = - sys.maxsize
player_name = ''
command = input()
while command != 'END':
    name_player = command
    goals = int(input())

    if goals > max_score:
        max_score = goals
        player_name = name_player
    if goals >= 10:
        break

    command = input()

if max_score >= 3:
    print(f'{player_name} is the best player!')
    print(f'He has scored {max_score} goals and made a hat-trick !!!')
elif max_score < 3:
    print(f'{player_name} is the best player!')
    print(f'He has scored {max_score} goals.')



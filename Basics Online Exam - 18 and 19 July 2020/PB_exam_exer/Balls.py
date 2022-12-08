balls_number = int(input())

red = 0
orange = 0
yellow = 0
white = 0
black = 0
other_colors = 0
points = 0

for i in range(balls_number):
    colors = input()
    if colors == 'red':
        points += 5
        red += 1
    elif colors == 'orange':
        points += 10
        orange += 1
    elif colors == 'yellow':
        points += 15
        yellow += 1
    elif colors == 'white':
        points += 20
        white += 1
    elif colors == 'black':
        points = points // 2
        black += 1
    else:
        other_colors += 1


print(f'Total points: {points}')
print(f'Red balls: {red}')
print(f'Orange balls: {orange}')
print(f'Yellow balls: {yellow}')
print(f'White balls: {white}')
print(f'Other colors picked: {other_colors}')
print(f'Divides from black balls: {black}')
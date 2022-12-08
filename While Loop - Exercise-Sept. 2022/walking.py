steps_counter = 0
line_input = input()
while line_input != 'Going home':
    current_steps = int(line_input)
    steps_counter += current_steps
    if steps_counter >= 10000:
        break

    line_input = input()

if line_input == 'Going home':
    home_steps = int(input())
    steps_counter += home_steps

diff = abs(steps_counter - 10000)

if steps_counter >= 10000:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
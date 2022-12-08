n = int(input())


for thousands in range(1, 10):
    for hundred in range(1, 10):
        for tens in range(1, 10):
            for units in range(1, 10):

                if n % thousands == 0 and n % hundred == 0 and n % tens == 0 and n % units == 0:
                    print(f'{thousands}{hundred}{tens}{units}', end=' ')

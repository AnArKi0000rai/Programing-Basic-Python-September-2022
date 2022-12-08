amount_of_food = int(input())

total_grams = amount_of_food * 1000
command = input()
while command != 'Adopted':
    current_data = int(command)
    total_grams -= current_data

    command = input()

if total_grams < 0:
    diff = abs(total_grams)
    print(f'Food is not enough. You need {diff} grams more.')
else:
    print(f'Food is enough! Leftovers: {total_grams} grams.')


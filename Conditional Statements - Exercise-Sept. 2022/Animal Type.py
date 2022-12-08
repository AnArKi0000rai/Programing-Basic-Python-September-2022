animal_type = input()

if animal_type in ('crocodile', 'tortoise', 'snake'):
    print('reptile')
elif animal_type == 'dog':
    print('mammal')
else:
    print('unknown')
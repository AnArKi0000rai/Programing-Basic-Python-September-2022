N1 = int(input())
N2 = int(input())
operator = input()

sum_number = 0
type_number = ''

if operator == '+':
    sum_number = N1 + N2
elif operator == '-':
    sum_number = N1 - N2
elif operator == '*':
    sum_number = N1 * N2
elif operator == '/' and N2 != 0:
    sum_number = N1 / N2
elif operator == '%' and N2 != 0:
    sum_number = N1 % N2

if sum_number % 2 == 0 and operator in ('+', '-', '*'):
    type_number = 'even'
else:
    type_number = 'odd'

if N2 == 0:
    print(f'Cannot divide {N1} by zero')
elif operator == '/':
    print(f'{N1} {operator} {N2} = {sum_number:.2f} ')
elif operator == '%':
    print(f'{N1} {operator} {N2} = {sum_number}')
elif operator in ('+', "-", "*"):
    print(f'{N1} {operator} {N2} = {sum_number} - {type_number}')


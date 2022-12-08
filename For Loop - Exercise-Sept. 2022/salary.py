tabs_number = int(input())
salary = int(input())

fine = 0
total_salary_fine = salary

for i in range(1, tabs_number + 1):
    name_website = input()
    if name_website == 'Facebook':
        fine += 150
    elif name_website == 'Instagram':
        fine += 100
    elif name_website == 'Reddit':
        fine += 50
    if fine >= total_salary_fine:
        print('You have lost your salary.')
        break

if total_salary_fine > fine:
    diff = abs(total_salary_fine - fine)
    print(diff)




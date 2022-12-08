judges = int(input())

sum_all_grades = 0
count_assessment = 0
data_input = input()
while data_input != 'Finish':

    sum_grades = 0
    for jury in range(1, judges + 1):
        grade = float(input())
        count_assessment += 1
        sum_grades += grade
        sum_all_grades += grade

    average_grade_for_each_presentation = sum_grades / judges
    print(f'{data_input} - {average_grade_for_each_presentation:.2f}.')

    data_input = input()

print(f"Student's final assessment is {sum_all_grades / count_assessment:.2f}.")
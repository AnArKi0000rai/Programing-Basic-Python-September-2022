unsatisfactory_appraisals = int(input())

bad_assessment = 0
assessment_count = 0
task_number = 0
last_task_name = ''
flag = False
input_line = input()
while input_line != 'Enough':
    task_name = input_line
    assessment = int(input())
    if assessment <= 4:
        bad_assessment += 1

    if bad_assessment >= unsatisfactory_appraisals:
        flag = True
        break

    task_number += 1
    assessment_count += assessment
    last_task_name = task_name
    input_line = input()

average_assessment = assessment_count / task_number
if flag:
    print(f"You need a break, {bad_assessment} poor grades.")
else:
    print(f'Average score: {average_assessment:.2f}')
    print(f'Number of problems: {task_number}')
    print(f'Last problem: {last_task_name}')



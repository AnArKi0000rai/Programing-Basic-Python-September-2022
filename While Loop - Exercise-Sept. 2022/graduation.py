name = input()

grade = 0
bad_rating = 0
total_assessment = 0

while True:
    current_assessment = float(input())
    grade += 1
    if current_assessment < 4:
        bad_rating += 1
        if bad_rating > 1:
            print(f'{name} has been excluded at {grade} grade')
            break
        grade -= 1
    else:
        total_assessment += current_assessment

    if grade == 12:
        average_assessment = total_assessment / grade
        print(f'{name} graduated. Average grade: {average_assessment:.2f}')
        break











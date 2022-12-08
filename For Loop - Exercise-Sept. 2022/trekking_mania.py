number_of_groups = int(input())

musalah = 0
montblank = 0
kilimanjaro = 0
k2 = 0
everest = 0
count_people = 0

for i in range (1, number_of_groups + 1):
    people_in_each_group = int(input())
    count_people += people_in_each_group
    if people_in_each_group <= 5:
        musalah += people_in_each_group
    elif people_in_each_group <= 12:
        montblank += people_in_each_group
    elif people_in_each_group <= 25:
        kilimanjaro += people_in_each_group
    elif people_in_each_group <= 40:
        k2 += people_in_each_group
    elif people_in_each_group > 40:
        everest += people_in_each_group


print(f'{(musalah / count_people) * 100:.2f}%')
print(f'{(montblank / count_people) * 100:.2f}%')
print(f'{(kilimanjaro / count_people) * 100:.2f}%')
print(f'{(k2 / count_people) * 100:.2f}%')
print(f'{(everest / count_people) * 100:.2f}%')
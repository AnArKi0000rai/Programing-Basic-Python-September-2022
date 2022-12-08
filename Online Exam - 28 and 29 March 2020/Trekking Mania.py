number_of_groups = int(input())

muslah = 0
monblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0
count_people = 0
for i in range(number_of_groups):
    people_in_the_group = int(input())
    count_people += people_in_the_group
    if people_in_the_group <= 5:
        muslah += people_in_the_group
    elif 6 <= people_in_the_group <= 12:
        monblanc += people_in_the_group
    elif 13 <= people_in_the_group <= 25:
        kilimandjaro += people_in_the_group
    elif 26 <= people_in_the_group <= 40:
        k2 += people_in_the_group
    elif people_in_the_group > 40:
        everest += people_in_the_group

percentage_of_climbing_musals = (muslah / count_people) * 100
percentage_of_climbers_of_Mont_Blanc = (monblanc / count_people) * 100
percentage_of_Kilimanjaro_climbers = (kilimandjaro/count_people) * 100
percentage_of_climbers_k2 = (k2 / count_people) * 100
percentage_of_Everest_climbers = (everest / count_people) * 100


print(f'{percentage_of_climbing_musals:.2f}%')
print(f'{percentage_of_climbers_of_Mont_Blanc:.2f}%')
print(f'{percentage_of_Kilimanjaro_climbers:.2f}%')
print(f'{percentage_of_climbers_k2:.2f}%')
print(f'{percentage_of_Everest_climbers:.2f}%')
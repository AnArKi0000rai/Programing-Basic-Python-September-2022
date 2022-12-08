import math

days_number = int(input())
amount_of_food = float(input())

count_dog_eats = 0
count_cat_eats = 0
biscuits = 0
for i in range(1, days_number + 1):
    dog_eats = int(input())
    count_dog_eats += dog_eats
    cat_eats = int(input())
    count_cat_eats += cat_eats
    if i % 3 == 0:
        biscuits += (dog_eats + cat_eats) * 0.10


total_food_amount = count_dog_eats + count_cat_eats
percent_of_eaten_food = (total_food_amount / amount_of_food) * 100

dogs_eaten = (count_dog_eats / total_food_amount) * 100
cats_eaten = (count_cat_eats / total_food_amount) * 100


print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{percent_of_eaten_food:.2f}% of the food has been eaten.')
print(f'{dogs_eaten:.2f}% eaten from the dog.')
print(f'{cats_eaten:.2f}% eaten from the cat.')
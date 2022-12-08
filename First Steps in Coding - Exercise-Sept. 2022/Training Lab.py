w = float(input())
h = float(input())

length = w // 1.20
width = (h - 1) // 0.7

number_of_places = (length * width) - 3

print(f'{number_of_places:.0f}')
num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
total_current_num = num

for i in range(1, num + 1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num <= 399:
        p2 += 1
    elif current_num <= 599:
        p3 += 1
    elif current_num <= 799:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

print(f'{p1 / total_current_num * 100:.2f}%')
print(f'{p2 / total_current_num * 100:.2f}%')
print(f'{p3 / total_current_num * 100:.2f}%')
print(f'{p4 / total_current_num * 100:.2f}%')
print(f'{p5 / total_current_num * 100:.2f}%')

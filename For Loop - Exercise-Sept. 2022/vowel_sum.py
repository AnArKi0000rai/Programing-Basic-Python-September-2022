word = input()

a = 1
e = 2
i = 3
o = 4
u = 5
sum_letters = 0

for letter in word:
    if letter == 'a':
        sum_letters += a
    elif letter == 'e':
        sum_letters += e
    elif letter == "i":
        sum_letters += i
    elif letter == 'o':
        sum_letters += o
    elif letter == 'u':
        sum_letters += u

print(sum_letters)




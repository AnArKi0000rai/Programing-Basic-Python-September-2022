change = float(input())
coins = change * 100
two_leva = 0
one_lev = 0
fifty_cent = 0
twenty_cent = 0
ten_cent = 0
five_cent = 0
two_cent = 0
one_cent = 0
while True:
    if coins >= 200:
        coins -= 200
        two_leva += 1
    elif coins >= 100:
        coins -= 100
        one_lev += 1
    elif coins >= 50:
        coins -= 50
        fifty_cent += 1
    elif coins >= 20:
        coins -= 20
        twenty_cent += 1
    elif coins >= 10:
        coins -= 10
        ten_cent += 1
    elif coins >= 5:
        coins -= 5
        five_cent += 1
    elif coins >= 2:
        coins -= 2
        two_cent += 1
    elif coins >= 1:
        coins -= 1
        one_cent += 1
    else:
        break

total_coins = two_leva + one_lev + fifty_cent + twenty_cent + ten_cent + five_cent + two_cent + one_cent

print(total_coins)

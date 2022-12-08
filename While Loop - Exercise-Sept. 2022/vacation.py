money_needed = float(input())
cash_available = float(input())

current_cash = cash_available
count_days = 0
spend_days = 0

while True:
    data = input()
    current_sum = float(input())
    count_days += 1
    if data == 'save':
        spend_days = 0
        current_cash += current_sum
    elif data == 'spend':
        current_cash -= current_sum
        if current_cash < 0:
            current_cash = 0
        spend_days += 1
        if spend_days == 5:
            print("You can't save the money.")
            print(count_days)
            break

    if current_cash >= money_needed:
        print(f'You saved the money for {count_days} days.')
        break




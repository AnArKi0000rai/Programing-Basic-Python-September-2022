days_of_stay = int(input())
room_type = input()
evaluation = input()

room_price = 0
night_of_stay = days_of_stay - 1

if room_type == "room for one person":
    room_price = night_of_stay * 18
elif room_type == 'apartment':
    room_price = night_of_stay * 25
    if night_of_stay < 10:
        room_price = room_price * 0.70
    elif 10 <= night_of_stay <= 15:
        room_price = room_price * 0.65
    elif night_of_stay > 15:
        room_price = room_price * 0.50
elif room_type == 'president apartment':
    room_price = night_of_stay * 35
    if night_of_stay < 10:
        room_price = room_price * 0.90
    elif 10 <= night_of_stay <= 15:
        room_price = room_price * 0.85
    elif night_of_stay > 15:
        room_price = room_price * 0.80

tips = 0

if evaluation == 'positive':
    tips = room_price * 0.25
    room_price = room_price + tips
elif evaluation == 'negative':
    tips = room_price * 0.90
    room_price = tips

print(f'{room_price:.2f}')





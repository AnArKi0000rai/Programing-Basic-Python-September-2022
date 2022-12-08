length_cm = int(input())
width_cm = int(input())
high_cm = int(input())
occupied_space = float(input())

tank_volume = length_cm * width_cm * high_cm
volume_in_liters = tank_volume / 1000
percent_occupied_space = occupied_space

litters_needed = ((volume_in_liters * percent_occupied_space) / 100)
total_liters_needed = volume_in_liters - litters_needed

print(total_liters_needed)
record_in_seconds = float(input())
distance_in_metres = float(input())
the_time_in_seconds_it_takes_to_climb_for_a_singular_m = float(input())

clime_time = distance_in_metres * the_time_in_seconds_it_takes_to_climb_for_a_singular_m
delay = (distance_in_metres // 50) * 30

total_time = clime_time + delay

if total_time >= record_in_seconds:
    diff = abs(total_time - record_in_seconds)
    print(f'No! He was {diff:.2f} seconds slower.')
else:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
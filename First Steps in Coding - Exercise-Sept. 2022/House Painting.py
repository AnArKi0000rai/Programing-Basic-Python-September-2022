house_height = float(input())
sidewall_length = float(input())
height_of_the_triangular_roof_wall = float(input())

sidewall_area = house_height * sidewall_length
window_area = (1.5 * 1.5) * 2
both_sidewalls_area = sidewall_area + sidewall_area - window_area
back_wall_area = house_height * house_height
enter_area = 1.2 * 2
total_back_and_front_walls = back_wall_area + back_wall_area - enter_area
total_area = both_sidewalls_area + total_back_and_front_walls
green_paint = total_area / 3.4

the_two_roof_rectangles = 2 * (house_height * sidewall_length)
the_two_roof_triangles = 2 * (house_height * height_of_the_triangular_roof_wall / 2)
total_roof_area = the_two_roof_rectangles + the_two_roof_triangles
red_paint = total_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
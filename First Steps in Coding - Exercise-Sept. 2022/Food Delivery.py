number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegan_menus = int(input())

chicken_menu_price = number_chicken_menus * 10.35
fish_menu_price = number_fish_menus * 12.40
vegan_menu_price = number_vegan_menus * 8.15

total_price_of_menus = chicken_menu_price + fish_menu_price + vegan_menu_price
price_of_dessert = total_price_of_menus * 0.20
delivery_price = 2.50

total_order_price = total_price_of_menus + price_of_dessert + delivery_price

print(total_order_price)
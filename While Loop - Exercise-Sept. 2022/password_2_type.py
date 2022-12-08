name = input()
password = input()
date = input()

while date != password:
    date = input()
else:
    print(f'Welcome {name}!')
# or print Welcome + name wthout else
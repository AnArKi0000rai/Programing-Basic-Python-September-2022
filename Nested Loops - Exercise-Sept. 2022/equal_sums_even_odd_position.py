init_sum = int(input())
end_sum = int(input())

for i in range(init_sum, end_sum + 1):

    hundred_thousands = i // 100000
    ten_thousands = (i // 10000) % 10
    thousands = (i // 1000) % 10
    hundreds = (i // 100) % 10
    tens = (i // 10) % 10
    units = i % 10

    even_num = ten_thousands + hundreds + units
    odd_num = hundred_thousands + thousands + tens

    if even_num == odd_num:
        print(i, end=' ')
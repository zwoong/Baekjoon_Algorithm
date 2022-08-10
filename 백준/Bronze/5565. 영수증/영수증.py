sum_price = int(input())

readable_price = 0
for i in range(9):
    price = int(input())
    readable_price += price

print(sum_price - readable_price)

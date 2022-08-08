n = int(input())

for _ in range(n):
    p = int(input())
    high_price = 0
    high_name = None
    for _ in range(p):
        C, N = input().split()
        if int(C) > high_price:
            high_price = int(C)
            high_name = N
    print(high_name)
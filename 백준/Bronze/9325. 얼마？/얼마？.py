T = int(input())

for _ in range(T):
    s = int(input())  # 자동차의 가격
    n = int(input())  # 옵션개수
    sum_price = s
    for _ in range(n):
        q, p = map(int, input().split())  # 자동차의 옵션으 개수 및 가격
        sum_price += q * p
    print(sum_price)
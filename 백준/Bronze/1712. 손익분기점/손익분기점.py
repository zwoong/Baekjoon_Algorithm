A, B, C = map(int, input().split())

# 손익분기점 = 총 고정비용 / (가격 - 가변비용) + 1
if B >= C:
    print("-1")
else:
    print(int(A / (C - B) + 1))

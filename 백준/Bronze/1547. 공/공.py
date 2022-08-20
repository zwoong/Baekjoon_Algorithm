M = int(input())  # 컵의 위치를 바꾼 횟수

location = 1

for _ in range(M):
    # 컵의 위치
    X, Y = map(int, input().split())
    if X == location:
        location = Y
    elif Y == location:
        location = X
print(location)

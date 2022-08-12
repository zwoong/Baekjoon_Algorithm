T = int(input())

left_apple = 0
for _ in range(T):
    S, A = map(int, input().split())
    left_apple += A % S
print(left_apple)
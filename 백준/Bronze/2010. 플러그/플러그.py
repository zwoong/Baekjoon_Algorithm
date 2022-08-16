import sys

input = sys.stdin.readline
N = int(input())  # 멀티탭의 개수

sum = 0
for _ in range(N):
    C = int(input())  # 플로그 개수
    sum += C

print(sum - (N - 1))

import sys

input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    V, E = map(int, input().split())
    print(-(V - E - 2))

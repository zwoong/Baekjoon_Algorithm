import sys

input = sys.stdin.readline

sum = 0
for _ in range(5):
    score = int(input())
    sum += score

print(sum)
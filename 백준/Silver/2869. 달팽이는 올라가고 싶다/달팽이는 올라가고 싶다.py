import math

a, b, v = map(int, input().split())
# a=5, b=1, v=6

answer = math.ceil((v - b) / (a - b))
#  5 / 4

print(answer)
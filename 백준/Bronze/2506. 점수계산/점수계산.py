n = int(input())
numbers = list(map(int, input().split()))

sum = 0
pre = 0
for i in numbers:
    if pre != 0 and i == 1:
        pre += 1
        sum += pre
    elif pre == 0 and i == 1:
        pre += 1
        sum += pre
    else:
        pre = 0

print(sum)

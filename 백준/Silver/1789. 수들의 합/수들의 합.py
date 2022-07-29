S = int(input())

i = 0
sum = 0

while S >= sum:
    if sum + i >= S:
        break
    i += 1
    sum += i

print(i)

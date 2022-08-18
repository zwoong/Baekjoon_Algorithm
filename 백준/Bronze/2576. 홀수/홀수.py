numlist = []
for i in range(0, 7):
    num = int(input())
    if num % 2 != 0:
        numlist.append(num)

if len(numlist) == 0:
    print(-1)
else:
    print(sum(numlist))
    print(min(numlist))

T = int(input())

for i in range(1, T + 1):
    array = list(map(str, input().split()))
    sum = 0
    for j in array:
        if j == "@":
            sum *= 3
        elif j == "%":
            sum += 5
        elif j == "#":
            sum -= 7
        else:
            sum += float(j)
    print(format(sum, ".2f"))

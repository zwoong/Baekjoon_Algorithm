listX = list()
listY = list()

for i in range(3):
    x, y = map(int, input().split())
    listX.append(x)
    listY.append(y)

for i in range(3):
    if listX.count(listX[i]) == 1:
        x_num = listX[i]

    if listY.count(listY[i]) == 1:
        Y_num = listY[i]

print(x_num, Y_num)
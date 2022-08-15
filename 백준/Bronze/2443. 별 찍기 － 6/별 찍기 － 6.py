N = int(input())

for i in range(0, N):

    b = " " * i + '*' * ((2 * N - 1) - (2 * i))
    print(b)

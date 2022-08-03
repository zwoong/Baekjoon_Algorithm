A = 300
B = 60
C = 10

T = int(input())

if T % C != 0 or T < 10:
    print(-1)
else:
    first = T // A
    if first != 0:
        T -= first * A

    second = T // B
    if second != 0:
        T -= second * B

    third = T // C

    print(first, second, third)
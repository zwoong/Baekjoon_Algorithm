S = int(input())
P = None

for i in range(1, S + 1):
    p = ""
    a, b = input().split()
    for j in b:
        p += j * int(a)
    print(p)

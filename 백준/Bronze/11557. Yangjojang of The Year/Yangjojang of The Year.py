T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    univ_name = None
    univ = 0
    for _ in range(1, N + 1):
        S, L = input().split()
        if int(L) > int(univ):
            univ_name = S
            univ = L
    print(univ_name)
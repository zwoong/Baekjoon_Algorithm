N = int(input())

for i in range(N):
    print(("*" * (N - int(i))).rjust(N))

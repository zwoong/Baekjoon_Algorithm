N = int(input())

if N == 1:
    print("*")
else:
    for n in range(N):
        if n % 2 == 0:
            print("* " * N)
        else:
            print(" *" * N)

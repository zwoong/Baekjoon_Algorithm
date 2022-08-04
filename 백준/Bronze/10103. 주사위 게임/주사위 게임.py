n = int(input())

changyoung = 100
jungsu = 100

for _ in range(1, n + 1):
    A, B = map(int, input().split())
    if A == B:
        continue
    elif A > B:
      jungsu -= A
    else:
      changyoung -= B

print(changyoung)
print(jungsu)
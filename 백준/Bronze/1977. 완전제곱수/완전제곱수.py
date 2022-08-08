import math

m = int(input())
n = int(input())

r = []
for i in range(math.ceil(m**0.5), int(n**0.5) + 1):
    r.append(i**2)
if r:
    print(sum(r), r[0], sep="\n")
else:
    print(-1)

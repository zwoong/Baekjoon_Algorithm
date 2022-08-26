cut = int(input())
piece = 1
a = 1
for i in range(cut):
    # 홀수라면
    if i % 2 != 0:
        a += 1
    piece += a
print(piece)

C = list(map(str, input()))

height = 0  # 높이
pre_sign = None

for i in C:
    if height == 0:
        height += 10
    elif pre_sign == i:
        height += 5
    else:
        height += 10
    pre_sign = i

print(height)

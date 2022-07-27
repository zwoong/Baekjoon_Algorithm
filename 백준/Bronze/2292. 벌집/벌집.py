n = int(input())
c = 1
while n > 1:  # n>0이 아닌 n>1인 이유는 입력이 1인 경우를 거르기 위해
    n -= (6 * c)
    c += 1
print(c)

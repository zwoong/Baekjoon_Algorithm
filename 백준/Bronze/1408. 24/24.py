h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

total = (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1)

if total < 0:
    total += 60 * 60 * 24

real_hour = total // 3600
real_min = (total % 3600) // 60
real_sec = total % 60

print("{0:02d}:{1:02d}:{2:02d}".format(real_hour, real_min, real_sec))
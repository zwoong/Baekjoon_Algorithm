sum_num = 0
idx = 0
for i in range(5):
    numbers = list(map(int, input().split()))
    print
    if sum_num < sum(numbers):
        sum_num = sum(numbers)
        idx = i + 1

print(idx, sum_num)

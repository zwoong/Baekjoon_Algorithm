numbers = list(map(int, input().split()))

squared_numbers = list()
for i in numbers:
    squared_numbers.append(i * i)

print(sum(squared_numbers) % 10)
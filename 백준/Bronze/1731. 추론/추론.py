n = int(input())
data = []

for _ in range(n):
    data.append(int(input()))

value = data[-1]

if data[2] - data[1] == data[1] - data[0]:
    value += data[2] - data[1]
else:
    value *= data[2] // data[1]

print(value)

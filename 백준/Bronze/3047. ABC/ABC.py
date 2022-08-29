num_list = list(map(int, input().split()))
order = input()

num_list.sort()
new_num_list = []
for s in order:
    if s == "A":
        new_num_list.append(num_list[0])
    elif s == "C":
        new_num_list.append(num_list[2])
    else:
        new_num_list.append(num_list[1])
print(*new_num_list)

num_list = []
for i in range(10):
    num_list.append(int(input()) % 42)
    
set_num_list = set(num_list)
new_number_list = list(set_num_list)
print(len(new_number_list))



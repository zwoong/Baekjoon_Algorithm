FBI_LIST = []
for i in range(1, 5 + 1):
    agent = input()
    if agent.find("FBI") != -1:
        FBI_LIST.append(i)

if len(FBI_LIST) == 0:
    print("HE GOT AWAY!")
else:
    print(*FBI_LIST)

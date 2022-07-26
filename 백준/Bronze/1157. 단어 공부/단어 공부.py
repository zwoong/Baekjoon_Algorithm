s = input().lower()
new_s = set(s)

cnt = 0
str = set()

for i in new_s:
    if cnt < s.count(i):
        cnt = s.count(i)

for i in new_s:
    if cnt == s.count(i):
        str.add(i)

if len(str) > 1:
    print("?")
else:
    list = list(str)
    print(list[0].upper())

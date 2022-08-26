Adrian_pick = ["A", "B", "C"]
Bruno_pick = ["B", "A", "B", "C"]
Goran_pick = ["C", "C", "A", "A", "B", "B"]

Adrian_cnt = 0
Bruno_cnt = 0
Goran_cnt = 0

T = int(input())
strs = input()
for i in range(T):
    if strs[i] == Adrian_pick[i % 3]:
        Adrian_cnt += 1

    if strs[i] == Bruno_pick[i % 4]:
        Bruno_cnt += 1

    if strs[i] == Goran_pick[i % 6]:
        Goran_cnt += 1

m = max(Adrian_cnt, Bruno_cnt, Goran_cnt)
print(m)
if m == Adrian_cnt:
    print("Adrian")
if m == Bruno_cnt:
    print("Bruno")
if m == Goran_cnt:
    print("Goran")

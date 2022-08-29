R, C, ZR, ZC = map(int, input().split())

article_arr = []
for _ in range(R):
    article = input()  # 기사
    res_article = ""
    for s in article:
        res_article += s * ZC
    for _ in range(ZR):
        article_arr.append(res_article)

for i in article_arr:
    print(i)

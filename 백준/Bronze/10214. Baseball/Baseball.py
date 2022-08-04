T = int(input())

for _ in range(1, T + 1):
    yonsei_score = 0
    korea_score = 0
    for _ in range(9):
        Y, K = map(int, input().split())
        yonsei_score += Y
        korea_score += K

    if yonsei_score == korea_score:
        print("Draw")
    elif yonsei_score > korea_score:
        print("Yonsei")
    else:
        print("Korea")

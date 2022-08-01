N = int(input())  # 참여하는 사람 수

reward = list()
for i in range(N):
    A, B, C = map(int, input().split())
    if A == B == C:
        reward.append(10000 + A * 1000)
    elif A == B:
        reward.append(1000 + A * 100)
    elif B == C:
        reward.append(1000 + B * 100)
    elif A == C:
        reward.append(1000 + A * 100)
    else:
        if B <= A >= C:
            reward.append(A * 100)
        elif A <= B >= C:
            reward.append(B * 100)
        else:
            reward.append(C * 100)

print(max(reward))
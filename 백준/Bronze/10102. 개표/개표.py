V = int(input())  # 심사위원의 수
participant = list(map(str, input()))  # 심사위원 투표 결과

A = participant.count("A")
B = participant.count("B")

if A == B:
    print("Tie")
elif A > B:
    print("A")
else:
    print("B")

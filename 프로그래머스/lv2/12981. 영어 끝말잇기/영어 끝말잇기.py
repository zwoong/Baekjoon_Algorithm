def solution(n, words):
    answer = []
    answer1 = [0,0]
    answer2 = []

    num = 0 # 번호
    cnt = 0 # 차례 

    arr = []
    # 배열안에 똑같은 문자가 있는지 체크
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == words[j]:
                arr.append(j)                 
    
    if len(arr) >= 1:
        arr.sort()
        answer1 = [arr[0] % n + 1, int(arr[0] / n) + 1]
    
    # word가 몇개인지 => for문을 몇번을 돌려야하는지
    for i in range(len(words)):

        # out of range 
        if i == len(words) - 1:
            answer2 = [0, 0]
            break 

        # words 배열에 전 글자에 맨 마지막 문자
        curr = words[i][-1]

        # words 배열에 현재 글자에 맨 앞 문자
        forward = words[i+1][0]

        # 끝말잇기 실패
        if curr != forward:
            answer2 = [(i+1) % n + 1, int((i+1) / n) + 1]
            break
            
    if answer1[1] == 0:
        answer = answer2
    elif answer2[1] == 0:
        answer = answer1
    else:
        # answer1 길이가 0인지 체크
        if answer1[1] == answer2[1]:
            if answer1[0] >= answer2[0]:
                answer = answer2
            else:
                answer = answer1
        elif answer1[1] > answer2[1]:
            answer = answer2
        else:
            answer = answer1

    return answer



n = int(input()) 

for i in range(n):
    score = list(map(str, input()))
 
    sum = 0
    answer = 0
    for i in range(len(score)):
    
        if score[i] == "O":
            sum += 1 + answer
            answer += 1 
        else:
            answer = 0
    print(sum)
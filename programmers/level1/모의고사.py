def solution(answers):
    answer = []
    answer1 = []
    p1 = [1,2,3,4,5]*2000
    p2 = [2,1,2,3,2,4,2,5]*1250
    p3 = [3,3,1,1,2,2,4,4,5,5]*1000
    player = [p1, p2, p3]

    for i in range(3):
        m = 0
        for j in range(len(answers)):
            m+=1
            if (player[i][j] == answers[j]):
                m += 1
        answer1.append(m)

    maxvalue = max(answer1)

    for k in range(3):
        if (maxvalue == answer1[k]):
            answer.append(k+1)

    return answer

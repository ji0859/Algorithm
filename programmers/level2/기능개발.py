import math
def solution(progresses, speeds):
    answer = [0]
    value = math.ceil((100-progresses[0])/speeds[0])

    for i, j in zip(progresses, speeds):
        if (value >= math.ceil((100-i)/j)):
            answer.append(answer.pop()+1)
        if (value < math.ceil((100-i)/j)):
            value = math.ceil((100-i)/j)
            answer.append(1)

    return answer

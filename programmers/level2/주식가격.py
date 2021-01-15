def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    for i in range(len(prices)):
        cnt = 1
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j] :
                answer[i] = cnt
                break;
            else:
                cnt+=1
    return answer

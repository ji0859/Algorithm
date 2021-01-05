def solution(n):
    answer = 0
    if n == 0:
        return 0
    for i in range(n+1):
        for j in range(n+1):
            if i * j == n:
                print(i, j)
                answer += i
    return answer

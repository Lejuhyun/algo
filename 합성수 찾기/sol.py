def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(2, n):
            if j != i:
                if i % j == 0:
                    answer = answer + 1
                    break
    return answer



print(solution(15))
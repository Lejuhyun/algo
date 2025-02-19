def solution(n):
    answer = 0
    k = n ** 0.5 
    if type(k) == int:
        answer =1
    else:
        answer = 2
    return answer

print(solution(144))
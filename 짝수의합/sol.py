def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer = answer + i
        else:
            pass
    return answer

print(solution(10))
print(solution(4))
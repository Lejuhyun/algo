

def solution(n, k): 
    # n : 양꼬치 인분수 / k: 음료수개수
    answer = 0
    if n < 10:
        answer = 12000* n + 2000 * k
        return answer
    else:
        answer = 12000 * n + 2000 * (k-n//10)
        return answer



print(solution(10,3))
print(solution(64,6))
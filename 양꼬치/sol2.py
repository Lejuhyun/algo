####solution2
def solution(n,k):
    answer=0
    if n >= 10:
        service= n//10
        answer= n * 12000 + (k-service) * 2000
    else:
        answer = n * 12000 + k * 2000
    return answer
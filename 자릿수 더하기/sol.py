
def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer = answer + int(i)
    return answer

print(solution(930211))
print(solution(1234))
def solution(my_string):
    answer = 0
    for i in my_string:
        if i in ['1','2','3','4','5','6','7','8','9']:
            answer = answer + int(i)
    return answer


# 두번째 방법
num=[]
for i in range(1,10):
    j = str(i)
    num.append(j)
print(num)

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))
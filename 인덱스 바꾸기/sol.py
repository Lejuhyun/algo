def solution(my_string, num1, num2):
    i = list(my_string)
    j = my_string[num1] 
    k = my_string[num2]
    i[num1] = k
    i[num2] = j


    result = "".join(i)
    return result




print(solution("hello", 1, 2))  # hlelo
print(solution("I love you", 3, 6))

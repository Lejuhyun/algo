def solution(my_string,letter):
    answer=''

    for char in my_string:
        if char != letter:
            answer = answer + char  ##문자열끼리의 덧셈 '' + 'a' = 'a'
                                    ## 'a' + 'b' = 'ab'

    return answer


print(solution('abcdef','f'))
print(solution('BCBdbe','B'))
print(solution('abcde','z'))
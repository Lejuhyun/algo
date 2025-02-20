def solution(my_string):
    my_list = list(my_string)
    my_list2 = my_list.reverse()
    print(my_list2)
    result = ''.join(my_list2)
    return result



print(solution("jaron"))
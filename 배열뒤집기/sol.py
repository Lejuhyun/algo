def solution(num_list):
    answer = []
    length=len(num_list)
    for i in range(length):
        num_list[i] = num_list[length-1-i]
    for i in range(length):
        answer = [num_list[i]]
    return answer



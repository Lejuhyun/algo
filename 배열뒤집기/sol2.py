def solution(num_list):
    answer = num_list
    length=len(num_list)
    for i in range(length):
        num_list[i] = num_list[length-1-i]
    return answer

print(solution([1, 2, 3, 4, 5]))

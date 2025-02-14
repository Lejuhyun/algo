def solution(num_list):
    answer = num_list

    temp_list = [0,0,0,0,0]


    length=len(num_list)
    for i in range(length):
        print(length-1-i)
        temp_list[i] = num_list[length-1-i]
    
    return temp_list

print(solution([1, 2, 3, 4, 5]))

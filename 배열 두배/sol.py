def twice(x):
    return x * 2


def solution(numbers):
    answer = map(twice, numbers)
    return list(answer)
    
    
print(solution([1, 2, 3, 4, 5]))
def solution(numbers):
    n = len(numbers)
    #.sort() 간단하게 원리만 이해하기
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers[-1] * numbers[-2]
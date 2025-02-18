def solution(numbers):
    answer = ''
    numbers.sort(reverse=True)
    answer = numbers[0]*numbers[1]
    return answer


def solution(numbers):
    answer = ''
    numbers.sort()
    answer = numbers[-1]*numbers[-2]
    return answer
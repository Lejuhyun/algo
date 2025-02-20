def solution(my_string):
    answer = 0

    for char in my_string:
        try: #일단 시도해보고 에러가 있는 경우/ 에러가 없는 경우 다른 행동을 취함
            answer += int(char)  #글자는 int취하면 ERROR가 나옴 -> except
        except:
            continue #다음 코드를 진행해주세요
        print(int(char))

    return answer
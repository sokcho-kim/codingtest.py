def solution(num):
    answer = 0
    while num != 1 : 
        if num % 2 == 0 : 
            num = int(num / 2)
        elif num % 2 == 1 : 
            num = int(num * 3 + 1) 
        else : 
            if num == 1 :
                return answer
        answer += 1 
    if answer > 500 : 
        answer = -1
    return answer
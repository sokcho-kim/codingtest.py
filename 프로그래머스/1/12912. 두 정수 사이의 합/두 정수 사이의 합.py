def solution(a, b):
    answer = 0
    mini = 0 
    maxi = 0 

    if a > b : 
        mini = b 
        maxi = a
    else:
        mini = a 
        maxi = b

    for i in range(mini,maxi+1):
        answer += i  
    return answer
def solution(x, n):
    answer = []
    
    for i in range(n) : 
        curr = x 
        curr = curr + i*x
        answer.append(curr)
    
    return answer
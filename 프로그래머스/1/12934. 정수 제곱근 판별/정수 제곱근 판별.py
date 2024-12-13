def solution(n):
    answer = 0
    low = 0 
    high = n 
    x = 0 
    while low <= high : 
        mid = (low + high)//2
        mid_sqrd = mid * mid 
        if mid_sqrd == n:
             x = mid
             break
        elif mid_sqrd < n:
            result = mid  
            low = mid + 1 
        else:
            high = mid - 1 
    if (x <= 0): answer = -1 
    else : answer = (x+1)**2
    
    return answer
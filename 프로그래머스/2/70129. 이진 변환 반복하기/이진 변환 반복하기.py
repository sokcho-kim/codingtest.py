def solution(s):
    chg_count = 0 
    remove_zeros = 0 

    while s != "1":
        zeros_cnt = s.count('0')
        remove_zeros += zeros_cnt
        
        s = s.replace('0', '')
        
        s = bin(len(s))[2:]  
        
        chg_count += 1

    return [chg_count, remove_zeros]
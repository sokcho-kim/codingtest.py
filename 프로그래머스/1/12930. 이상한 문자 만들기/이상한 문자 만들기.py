def solution(s):
    answer = ''
    copy_s = s.split(" ") 
    for idx, item in enumerate(copy_s): 
        for i in range(len(item)): 
            if i % 2 == 0: 
                answer += item[i].upper() 
            else: 
                answer += item[i].lower()
        
        if idx < len(copy_s) - 1:
            answer += " "
    return answer
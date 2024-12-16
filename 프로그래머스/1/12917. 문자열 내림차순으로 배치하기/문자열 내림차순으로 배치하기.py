
def solution(s):
    answer = ''
    print(s)
    lower_lst = list()
    upper_lst = list()
    for c in s : 
        if c.islower() : 
            lower_lst.append(c)
        else : 
            upper_lst.append(c)
    answer = sorted(lower_lst,reverse=True)+sorted(upper_lst,reverse=True)
    answer = ''.join(answer) 
    return answer

def solution(s):
    answer = ''
    arr_s = s.split(" ")
    int_s = list()
    for item in arr_s : 
        int_s.append(int(item))
    answer = str(min(int_s))+" "+str(max(int_s))
    return answer
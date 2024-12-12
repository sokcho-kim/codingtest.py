def solution(n):
    answer = 0
    str_n = list(str(n))
    reverse_n = sorted(str_n)
    ret_str = "" 

    for i in range(len(reverse_n)-1,-1,-1):
      ret_str += reverse_n[i] 

    answer = int(str(ret_str))

    return answer
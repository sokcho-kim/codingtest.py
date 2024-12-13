def solution(x):
    answer = True
    str_x = str(x)
    sum_x = 0 

    for i in str_x: 
      sum_x += int(i) 

    if x % sum_x == 0 : 
      answer = True
    else :
      answer = False
    return answer
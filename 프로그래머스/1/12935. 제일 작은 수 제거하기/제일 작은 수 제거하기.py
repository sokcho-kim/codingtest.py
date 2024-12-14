def solution(arr):
    answer = []
    answer = arr
    arr_temp = sorted(arr)

    if len(arr)<= 1 : 
      answer.clear()
      answer.append(-1)
    else :
      answer.remove(arr_temp[0])
      
    return answer
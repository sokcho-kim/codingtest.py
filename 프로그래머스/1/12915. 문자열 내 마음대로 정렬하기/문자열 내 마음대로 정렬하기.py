def solution(strings, n):
    answer = []
    sort_arr = []
    for i in strings : 
      sort_arr.append([i[n], i])

    temp = sorted(sort_arr)

    for item in temp : 
      answer.append(item[1])
  
    return answer
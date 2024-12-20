def solution(t, p):
    answer = 0
    interval = len(p)

    for i in range(len(t)) : 
      target = i+interval
      if target <= len(t) : 
        if t[i:target] <= p : 
          answer += 1 
    return answer
  
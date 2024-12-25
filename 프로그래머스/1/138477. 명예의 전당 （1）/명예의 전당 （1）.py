def solution(k, score):
    answer = []
    ans = []
    for i, item in enumerate(score) : 
      if len(ans) < k : 
        ans.append(item)
      else :  
        if item >= min(ans): 
          ans.remove(min(ans))
          # ans.pop(0)
          ans.append(item)
      answer.append(min(ans))
      # ans.sort()
    return answer
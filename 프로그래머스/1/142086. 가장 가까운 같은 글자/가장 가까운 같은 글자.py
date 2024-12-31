def solution(s):
    answer = []
    where = {} 
    for i, item in enumerate(list(s)) :
      if item not in where : 
        answer.append(-1)
      else : 
        answer.append(i-where[item])
      where[item] = i 
    return answer
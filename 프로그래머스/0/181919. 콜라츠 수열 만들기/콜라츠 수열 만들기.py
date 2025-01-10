def solution(n):
    answer = []
    while n >= 1 : 
      answer.append(n)
      if n ==1 : 
        break
      elif n % 2 == 0 : 
        n = n//2
      else : 
        n = n*3+1
    return answer
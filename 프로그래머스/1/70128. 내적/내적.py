def solution(a, b):
    answer = 0

    for i in range(len(a)) : 
      print(a[i]*b[i])
      answer += a[i]*b[i]
        
    return answer
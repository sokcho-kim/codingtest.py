def solution(n):
    answer = ''
    pattern ="수박"
    div = int(n/len(pattern))
    if n%2 == 0 : 
      answer = pattern * div
    else : 
      answer = pattern * div + pattern[0]
    return answer
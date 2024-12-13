def solution(seoul):
    answer = ''
    pointer= 0 
    for i in range(len(seoul)) : 
      if seoul[i] == "Kim" : 
        pointer = i 
    answer = f"김서방은 {pointer}에 있다"
    return answer
def solution(s):
    answer = ''
    i = int(len(s)/2)
    if len(s) %2 == 0 :
      answer = s[i-1:i+1]
    else:
      answer = s[i]
    return answer

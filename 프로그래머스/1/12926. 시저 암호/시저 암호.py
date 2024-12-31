import string 

def solution(s, n):
    answer = ''
    upper_alphabet = list(string.ascii_uppercase)
    lower_alphabet = list(string.ascii_lowercase)
    
    for c in s : 
      if c.isupper() :
        idx = upper_alphabet.index(c)
        push_idx = (idx + n) % 26
        answer += upper_alphabet[push_idx]
      elif c.islower():
        idx = lower_alphabet.index(c)
        push_idx = (idx + n) % 26
        answer += lower_alphabet[push_idx]
      else :
        answer += " "
      
    return answer
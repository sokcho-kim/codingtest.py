def solution(clothes):
    answer = 0
    dict_clothes = dict()
    for item, category in clothes:
      if category not in dict_clothes:
        dict_clothes[category] = 0
      dict_clothes[category] += 1

    answer = 1 
    for cnt in dict_clothes.values() : 
      answer *= (cnt+1)

    answer -= 1 

    return answer
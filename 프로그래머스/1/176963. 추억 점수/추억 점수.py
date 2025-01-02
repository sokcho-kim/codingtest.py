def solution(name, yearning, photo):
    answer = []
    name_year = dict() 
    ans_dict = dict()

    for i in range(len(name)) : 
      name_year[name[i]] = yearning[i]   
    
    for arr in photo : 
      photo_value = 0 
      for item in arr : 
        if item in name_year : 
          photo_value += name_year[item]
          # print(photo_value)
      answer.append(photo_value)

    return answer
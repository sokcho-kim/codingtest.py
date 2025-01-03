class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
          "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
        }
        roman_dict2 = {
            "IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900
        }
        answer = 0 

        for k,v in roman_dict2.items() : 
            if k in s : 
                answer += v
                s = "".join(s.split(k))
        
        for i in s : 
            answer += int(roman_dict[i])
      
        return answer 
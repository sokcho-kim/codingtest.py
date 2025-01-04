class Solution:
  def intToRoman(self, num: int) -> str:
      roman_dict = {
          1 : "I", 4 : "IV", 5 : "V",  9 : "IX", 10 : "X", 40 : "XL", 50 : "L", 
          90 : "XC", 100 : "C",400 : "CD", 500 : "D", 900 : "CM" , 1000 : "M"
      }
      answer = ""

      for k in reversed(roman_dict.keys()) :
        while num >= k : 
          answer += roman_dict[k]
          num -= k 
      
      return answer
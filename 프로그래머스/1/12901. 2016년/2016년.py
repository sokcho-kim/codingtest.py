def solution(a, b):
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    total_days = sum(month_days[:a]) + b  
    
    weekday_index = (total_days - 1 + 5) % 7 
    
    return weekdays[weekday_index]
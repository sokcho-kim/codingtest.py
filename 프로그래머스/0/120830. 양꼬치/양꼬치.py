def solution(n, k):
    answer = 0
    # 10일때마다 음료수 값 -1 
    discount = (n//10) * 2000
    answer = (12000 * n) + (2000*k) - discount 

    return answer
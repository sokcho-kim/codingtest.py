def solution(left, right):
    answer = 0
    for num in range(left,right+1) : 
        sqrt = num**(1/2)
        prime_list = list()
        for i in range(1,num+1) : 
            if num % i == 0 : 
                prime_list.append(i)
        if len(prime_list) % 2 == 0 : 
            answer += num 
        else : 
            answer -= num
    return answer

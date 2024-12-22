def solution(prices):
    n = len(prices)
    answer = [0] * n  # 결과 배열을 0으로 개수만큼 초기화 (기간이니깐 매개변수 개수만큼 필요)
    stack = []  # 스택 만들기 

    for i in range(n):
        # 스택이 비어 있지 않으면 현재 가격이 스택의 top 가격보다 작을 때까지 pop
        while stack and prices[stack[-1]] > prices[i]:
            index = stack.pop()  # 인덱스를 pop하여 가져온다
            answer[index] = i - index  # 떨어지지 않은 기간 계산
        
        stack.append(i)  # 현재 인덱스를 스택에 추가

    # 스택에 남아있는 인덱스는 떨어지지 않은 기간을 계산
    while stack:
        index = stack.pop() 
        answer[index] = n - 1 - index  #마지막 인덱스까지의 차이(전체 길이 -1-인덱스)

    return answer


def solution(n, left, right):
    answer = []
    
    
    # 처음에는 하란대로 빈 배열 세팅 해서 했지만 다 하고나서 부질 없음을 깨달음 ㅡㅡ 
    for i in range(left, right + 1): # 처음에는 순진하게 1부터 시작했지만 그것도 부질 없음을 깨달음 ㅡㅡ 두번 일함 
        # 행열은 1차원 입장에서 계산 
        row = i // n  # 행 계산 : 현재 인덱스가 속한 행 
        col = i % n   # 열 계산 : 현재 인덱스가 속한 열 
        # 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
        # 위치값의 최대이기 때문에 max (이딴걸 왜하지 처음에 문제 이해 못함 ㅡㅡ)
        #    0   1   2 
        # 0  1   2   3 
        # 1  2   2   3
        # 2  3   3   3
        value = max(row + 1, col + 1)  # 이새끼는 2차원 입장 
        answer.append(value) #필요한 새끼만 추출 
    
    return answer
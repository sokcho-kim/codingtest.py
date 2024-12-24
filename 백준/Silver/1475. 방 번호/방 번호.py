n = input()

be_char = str(n)
# 1. 같은 숫자가 1번 이상 등장하면 등장 최대 값이 세트의 수
# 2. 다만 6이나 9의 경우는 뒤집으면 되기 때문에 발생 빈도//2 
freq = [0] * 10  # 0부터 9까지의 발생빈도 저장할 배열 초기화 

# 각 숫자의 출현 빈도
for char in be_char:
    freq[int(char)] += 1  # 문자열을 정수로 변환하여 인덱스에 추가

# 6과 9의 빈도 합산
set_6_9 = (freq[6] + freq[9] + 1) // 2  # 반올림 귀찮다 

# 나머지 숫자 중 최대 빈도 
max_other_cnt = 0
for i in range(10):
    if i != 6 and i != 9:  # 6과 9 제외
        max_other_cnt = max(max_other_cnt, freq[i])

# 누가 더 크니 
answer = max(max_other_cnt, set_6_9)

print(answer)

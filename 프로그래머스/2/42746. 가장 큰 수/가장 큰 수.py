def merge_sort(numbers):
    # 리스트의 길이가 1 이하이면 그대로 반환
    if len(numbers) <= 1:
        return numbers

    # 리스트를 중간에서 나누기
    mid = len(numbers) // 2
    left_half = merge_sort(numbers[:mid])
    right_half = merge_sort(numbers[mid:])

    # 병합 단계
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] + right[0] > right[0] + left[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    # 남은 요소들을 결과에 추가
    result.extend(left)
    result.extend(right)
    
    return result

def solution(numbers):
    # 숫자들을 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 병합 정렬을 사용하여 숫자 정렬
    sorted_numbers = merge_sort(str_numbers)
    
    # 정렬된 숫자들을 이어 붙여 가장 큰 수 생성
    largest_number = ''.join(sorted_numbers)
    
    # 모든 숫자가 '0'인 경우 '0' 반환
    if largest_number[0] == '0':
        return '0'
    
    return largest_number
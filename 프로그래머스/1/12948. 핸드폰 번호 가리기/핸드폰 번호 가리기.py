def solution(phone_number):
    answer = ''
    cnt_front = len(phone_number)-4
    answer = ('*'*cnt_front)+phone_number[-4:]
    return answer

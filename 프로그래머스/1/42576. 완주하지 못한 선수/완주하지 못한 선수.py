def solution(participant, completion):
    answer = ''
    parti_dict = dict() 

    # 참가자 수 세기
    for i in participant: 
        parti_dict[i] = parti_dict.get(i, 0) + 1
    
    # 완주자 수 줄이기
    for i in completion: 
        parti_dict[i] -= 1

    # 완주하지 못한 참가자 찾기
    for key, value in parti_dict.items():
        if value > 0:
            answer = key
            break

    return answer

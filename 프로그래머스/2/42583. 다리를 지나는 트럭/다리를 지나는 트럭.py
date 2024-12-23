from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)  
    total_weight = 0 

    for truck in truck_weights:
        while True:
            answer += 1
            
            total_weight -= bridge.popleft()

            if total_weight + truck <= weight:
                bridge.append(truck)  
                total_weight += truck 
                break
            else:
                bridge.append(0)  

    return answer + bridge_length
def solution(nums):
    answer = 0
    
    nums2 = set(nums)
    nums3 = list(nums2)
    
    cnt_rt = int(len(nums)/2)
    cnt_no_duple = len(nums3)

    if cnt_no_duple <= cnt_rt : 
        answer = cnt_no_duple
    else : 
        answer = cnt_rt
        
    return answer


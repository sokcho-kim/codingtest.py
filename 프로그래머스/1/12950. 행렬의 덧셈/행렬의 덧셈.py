def solution(arr1, arr2) : 
    answer = list()
    for i in range(len(arr1)):
        sublist = list()
        for j in range(len(arr1[i])):  
            sublist.append(arr1[i][j] + arr2[i][j])
        answer.append(sublist)
    return answer
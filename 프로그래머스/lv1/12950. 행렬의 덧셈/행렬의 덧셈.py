def solution(arr1, arr2):
    answer_list = []
    tmp = []
    for i, v in zip(arr1,arr2):
        for a,b in zip(i,v):
            tmp.append(a+b)
        answer_list.append(tmp)
        tmp = []
    
    answer = [[]]
    return answer_list
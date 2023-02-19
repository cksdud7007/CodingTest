# import numpy as np
# def solution(arr1, arr2):
#     arr1 = np.array(arr1)
#     arr2 = np.array(arr2)
#     answer = arr1 @ arr2
#     return answer.tolist()
def solution(arr1,arr2):
    b = []
    for i in range(len(arr1)):
        a = []
        for j in range(len(arr2[0])):
            d = 0
            for k in range(len(arr1[0])):
                d += arr1[i][k] * arr2[k][j]
            a.append(d)
        b.append(a)
    return b
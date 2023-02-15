# def solution(arr):
#     a = [2,3,5,7]
#     d = []
#     k = []
#     o = []
#     count = 0
#     while True:
#         for i in a:    # [2,3,5,7]
#             for j in arr:   ### [12,24,36]
#                 if j % i == 0:
#                     d.append(True)
#                     k.append(j//i)
#                 else:
#                     k.append(j)
#                     d.append(False)
#             if sum(d)>=2:    # 만약 모두 나눠지는 정수가 있으면
#                 o.append(i)
#                 arr = k
#                 k = []
#                 d = []
#                 count += 1
#                 break
#             else:
#                 k = []
#                 d = []
#         if count == 1:
#             count = 0
#         else:
#             o.extend(arr)
#             break
#     h = 1
#     for i in o:
#         h *= i
#     return h

def solution(arr):
    from math import gcd                            
    answer = arr[0]                                 

    for num in arr:                              
        answer = answer*num // gcd(answer, num)     

    return answer
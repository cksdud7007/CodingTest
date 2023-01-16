## 당연히 시간초과
# def solution(arrayA, arrayB):
#     a = arrayA[0]
#     b = arrayB[0]
#     check1 = False
#     check2 = False
    
#     while a:
#         for idx in range(len(arrayA)):
#             if arrayA[idx] % a == 0 and arrayB[idx] % a != 0:
#                 check1 = True
#                 pass
#             else:
#                 check1 = False
#                 break
#         if check1:
#             break
#         a -= 1
        
    
#     while b:
#         for idx in range(len(arrayB)):
#             if arrayB[idx] % b == 0 and arrayA[idx] % b != 0:
#                 check2 = True
#                 pass
#             else:
#                 check2 = False
#                 break
#         if check2:
#             break
    
#         b -= 1
    
#     if check1 == False and check2 == True:
#         return b
#     elif check2 == False and check1 == True:
#         return a
#     elif check1 and check2:
#         return max(a,b)
#     else :
#         return 0

#### gcd 알고리즘 (최대 공약수)

from math import gcd

def get_gcd(arr):
    g = arr[0]
    for i in arr:
        g = gcd(g,i)
    return g

def solution(arrayA,arrayB):
    
    a = get_gcd(arrayA)
    b = get_gcd(arrayB)
    check = 0
    
    for i in arrayA:
        if i % b == 0:
            break
    else:
        check = max(check, b)
        
    for i in arrayB:
        if i % a == 0:
            break
    else:
        check = max(check, a)
        
    return check
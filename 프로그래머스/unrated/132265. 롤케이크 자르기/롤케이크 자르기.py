# 시간 초과
# from collections import deque

# def solution(topping):
#     cnt = 0
#     right_topping = deque(topping)
#     left_topping = set()
    
#     while right_topping:
#         left_topping.add(right_topping.popleft())
#         if len(left_topping) == len(set(right_topping)):
#             cnt += 1
#     return cnt

from collections import Counter
def solution(topping):
    right_topping = Counter(topping)
    left_topping = {}
    cnt = 0
    
    for topp in topping:
        if topp in left_topping:
            left_topping[topp] += 1
        else:
            left_topping[topp] = 1
        right_topping[topp] -= 1
        
        if right_topping[topp] == 0:
            del right_topping[topp]
            
        if len(left_topping) == len(right_topping):
            cnt += 1
            
    return cnt
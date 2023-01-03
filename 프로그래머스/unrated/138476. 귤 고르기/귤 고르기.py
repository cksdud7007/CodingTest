from collections import deque

def solution(k, tangerine):
    tangerine = deque(sorted(tangerine))
        
    start = tangerine.popleft()
    cnt = 1
    cnt_dict = {}
    while tangerine:
        point = tangerine.popleft()
        if start == point:
            cnt += 1
        else:
            cnt_dict[start] = cnt
            start = point
            cnt = 1
            
    cnt_dict[start] = cnt
    answer = 0    
    result = 0
    for i in sorted(cnt_dict.values(),reverse = True):
        answer += i
        result += 1
        if answer >= k:
            return result
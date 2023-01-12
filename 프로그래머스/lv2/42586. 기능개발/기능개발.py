# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer

from collections import deque
def solution(progresses,speeds):
    count_list = []
    for i,v in zip(progresses,speeds):
        a = i
        count = 0
        while True:
            count += 1
            a += v  
            if a >= 100:
                break
        count_list.append(count)
    que = deque()
    que.extend(count_list)
    num = que.popleft()
    new_count = 1
    new_count_list = []
    while True:
        if len (que) == 0:
            new_count_list.append(new_count)
            break
        if num >= que[0]:
            new_count +=1     
            que.popleft()
        else:
            new_count_list.append(new_count)
            num = que.popleft()
            new_count = 1
    
    return  new_count_list
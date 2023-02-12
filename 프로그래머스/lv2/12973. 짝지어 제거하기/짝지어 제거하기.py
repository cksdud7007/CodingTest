# def solution(s):
#     answer = []

#     for i in s:
#         if len(answer) ==0:
#             answer.append(i)
#         elif answer[-1] == i:
#             answer.pop()
#         else:
#             answer.append(i)
#     if len(answer) == 0:
#         return 1
#     else:
#         return 0
def solution(s):
    que = []
    que.append(s[0])
    for i in s[1:]:
        que.append(i)
        if len(que) ==1:
            continue
        if que[-1] == que[-2]:
            que.pop()
            que.pop()
    if len(que) == 0:
        return 1
    else:
        return 0
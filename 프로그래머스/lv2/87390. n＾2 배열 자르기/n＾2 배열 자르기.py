# 시간 초과
# def solution(n, left, right):
#     box = [[0] *n  for i in range(n)]
#     cnt = 0
#     def right_up(i,cnt):
#         j = 0
#         while j <= i:
#             box[i][j] = cnt
#             j += 1

#         while i:
#             i -= 1
#             box[i][j-1] = cnt 

#     for i in range(n):
#         cnt += 1
#         right_up(i,cnt) # 오른 위쪽

#     box_list = []
#     for i in range(n):
#         box_list.extend(box[i])

#     answer = box_list[left:right+1]
    
#     return answer

# 시간 초과 개선 => 행렬은 리스트의 몫과 나머지로 인덱스를 구할 수 있다

def solution(n,left,right):
    box_list = []
    for i in range(left,right + 1):
        a = i//n
        b = i%n
        box_list.append(max(i//n,i%n) + 1)
    return box_list
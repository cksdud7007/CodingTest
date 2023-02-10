# def solution(priorities, location):
#     priorities_tuple= []
#     for i,v in enumerate(priorities):
#         priorities_tuple.append([v,i])
    
#     for i in range(len(priorities_tuple)-1):
#         j = i + 1
#         while j != len(priorities_tuple):
#             if priorities_tuple[i][0] < priorities_tuple[j][0]:
#                 priorities_tuple.append(priorities_tuple.pop(i))
#                 j = i
#             j = j + 1
                
#     count = 0
#     for i in priorities_tuple:
#         count += 1
#         if i[1] == location:
#             return count
def solution(priorities,location):
    prior_list = []
    for i,v in enumerate(priorities):
        prior_list.append([v,i])
    for i in range(len(prior_list)-1):
        j = i + 1
        while True:
            if prior_list[i][0] < prior_list[j][0]:
                prior_list.append(prior_list.pop(i))
                j = i
            j += 1
            if j == len(prior_list):
                break
    count = 0
    print(prior_list)
    for i in prior_list:
        count += 1
        if i[1] == location:
            return count
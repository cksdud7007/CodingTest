def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[i])):
            idx = 0
            max_list = []
            while idx != len(land[i]):
                if idx == j:
                    idx += 1
                    continue
                else:
                    max_list.append(land[i][j] + land[i-1][idx])
                idx += 1
            land[i][j] = max(max_list)
    return max(land[len(land)-1])
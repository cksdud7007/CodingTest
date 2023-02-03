def solution(n):
    count = 0
    for i in range(1,n+1):
        count_list = []
        answer = True
        while answer:
            count_list.append(i)
            i += 1
            if sum(count_list) == n:
                count += 1
                answer = False
            elif sum(count_list) > n:
                answer = False
            
    return count
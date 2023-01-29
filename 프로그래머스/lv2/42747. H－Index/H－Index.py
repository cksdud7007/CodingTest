def solution(citations):
    
    n = len(citations)
    b = sorted(citations,reverse=True)
    count = 0
    for i in range(n):
        tmp = b[i]
        count += 1
        if tmp < count:
            count = count - 1
            break
    return count
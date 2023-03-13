from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    k = len(words)
    l = len(begin)
    visited = [False] * (k)
    queue = deque()
    queue.append([begin,0])
    while queue:
        check, cnt = queue.popleft()
        if check == target:
            return cnt
        for i in range(k):
            if visited[i]:
                continue
            count = 0
            for a,b in zip(check,words[i]):
                if a == b:
                    count += 1
            if count == l - 1:
                visited[i] = True
                queue.append([words[i] ,cnt + 1])
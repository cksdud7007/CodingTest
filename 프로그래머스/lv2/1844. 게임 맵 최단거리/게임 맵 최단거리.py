from collections import deque
def solution(maps):
    queue = deque()
    x,y = 0,0
    n = len(maps)
    m = len(maps[0])
    queue.append((x,y))
    dx = [0,0,1,-1] #동 서 남 북
    dy = [1,-1,0,0] #동 서 남 북
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny>= m:
                continue
            if maps[nx][ny] == 0:
                continue
            elif maps[nx][ny] ==1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))

    if maps[n-1][m-1] == 1:
        return -1        
    return maps[n-1][m-1]
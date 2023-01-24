def solution(dirs):
    
    direction = ["R","L","D","U"]
    dx = [1,-1,0,0]     # 동,서,남,북
    dy = [0,0,-1,1]
    n,start_x,start_y,count,end_nx,end_ny = 5,0,0,0,0,0
    answer = []
    for i in dirs:
        for j in range(len(direction)):
            if i == direction[j]:
                end_nx = (start_x + dx[j])
                end_ny = (start_y + dy[j])
                start = [start_x,start_y]
                end = [end_nx,end_ny]
                if -5<=end_nx<=5 and -5<=end_ny<=5:
                    if [start,end] in answer or [end,start] in answer:
                        start_x,start_y =end_nx,end_ny
                    else:
                        count += 1
                        start_x,start_y =end_nx,end_ny
                        answer.append([start,end])
    return count
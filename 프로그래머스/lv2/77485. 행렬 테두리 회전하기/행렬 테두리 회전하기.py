def solution(rows, columns, queries):
    k = 1
    squre = []
    for i in range(rows):
        a = []
        for j in range(columns):
            a.append(k)
            k += 1
        squre.append(a)
    stack = []
    min_answer = []
    for j in queries:
        start_x,start_y,end_x,end_y = j
        start_x = start_x - 1
        start_y = start_y - 1
        end_x = end_x - 1
        end_y = end_y - 1
        answer = []
        stack.append(squre[start_x][start_y])
        d = start_x
        b = start_y
        stack = []
        stack.append(squre[start_x][start_y])
        while start_y < end_y:
            stack.append(squre[start_x][start_y+1])
            answer.append(stack[0])
            squre[start_x][start_y+1] = stack.pop(0)
            start_y += 1
            if start_y == end_y:
                stack.append(squre[start_x+1][start_y])
                answer.append(stack[0])
                squre[start_x+1][start_y] = stack.pop(0)
                start_x += 1
        while start_x < end_x:
            stack.append(squre[start_x+1][start_y])
            answer.append(stack[0])
            squre[start_x+1][start_y] = stack.pop(0)
            start_x += 1
            if start_x == end_x:
                stack.append(squre[start_x][start_y-1])
                answer.append(stack[0])
                squre[start_x][start_y-1] = stack.pop(0)
                start_y -= 1
        while start_y > b:
            stack.append(squre[start_x][start_y-1])
            answer.append(stack[0])
            squre[start_x][start_y-1] = stack.pop(0)
            start_y -= 1
            if start_y == b:
                stack.append(squre[start_x-1][start_y])
                answer.append(stack[0])
                squre[start_x-1][start_y] = stack.pop(0)
                start_x -= 1
        while start_x > d:
            stack.append(squre[start_x-1][start_y])
            answer.append(stack[0])
            squre[start_x-1][start_y] = stack.pop(0)
            start_x -= 1
        min_answer.append(min(answer))
    return min_answer
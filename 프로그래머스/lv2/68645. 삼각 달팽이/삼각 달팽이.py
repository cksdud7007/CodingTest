# def goto_down(l, n_row, n_number, _n, _p):
#     if len(l[n_row]) == n_row+1:
#         return l, n_row, n_number, True
#     while _n > n_row and len(l[n_row]) != n_row+1:
#         n_number += 1
#         n_row += 1
#         l[n_row-1].append(n_number) if _p == 0 else l[n_row-1].insert(_p, n_number)
#     return l, n_row, n_number, False


# def goto_right(l, n_row, n_number, _n, _p):
#     if len(l[n_row-1]) == n_row:
#         return l, n_row, n_number, True
#     while len(l[n_row-1]) != n_row:
#         n_number += 1
#         _p += 1
#         l[n_row-1].insert(_p, n_number)
#     return l, n_row, n_number, False


# def goto_up(l, n_row, n_number, _n, _p):
#     if len(l[n_row-2]) == n_row-1:
#         return l, n_row, n_number, True
#     while len(l[n_row-2]) != n_row-1:
#         n_number += 1
#         n_row -= 1
#         l[n_row-1].append(n_number) if _p == 0 else l[n_row-1].insert(-_p, n_number)
#     return l, n_row, n_number, False


# def solution(n):
#     f = []
#     number = 1
#     row = 1
#     position = 0
#     for i in range(n):
#         f.append([])

#     f[row-1].append(number)
#     if n == 1:
#         return f[0]

#     while True:
#         f, row, number, DONE = goto_down(f, row, number, n, position)
#         if DONE is True:
#             return [i for sub in f for i in sub]
#         f, row, number, DONE = goto_right(f, row, number, n, position)
#         if DONE is True:
#             return [i for sub in f for i in sub]
#         f, row, number, DONE = goto_up(f, row, number, n, position)
#         if DONE is True:
#             return [i for sub in f for i in sub]
#         position += 1


# answer = []
# answer = solution(6)

# print(answer)


# answer = []
# answer = solution(6)

# print(answer)

def solution(n):
    arr = []
    for i in range(n):
        sub = []
        for j in range(n):
            sub.append(0)
        arr.append(sub)
    x = -1
    y = 0
    num = 0
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
                num += 1
                arr[x][y] = num
            if i % 3 == 1:
                y += 1
                num += 1
                arr[x][y] = num
            if i % 3 == 2:
                x -= 1
                y -= 1
                num += 1
                arr[x][y] = num
    k = []
    for i in arr:
        sub = []
        for j in i:
            if j != 0:
                k.append(j)
    return k
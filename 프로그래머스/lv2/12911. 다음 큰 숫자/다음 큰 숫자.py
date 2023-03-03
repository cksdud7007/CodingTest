# def ej(n):
#     a = ''
#     while n != 1:
#         a = str(n % 2) + a
#         n = n // 2
#     a = '1' + a
#     return a

def solution(n):
    b = n+1
    while True:
        if bin(n)[2:].count('1') == bin(b)[2:].count('1'):
            break
        b += 1
    return b
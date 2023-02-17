def solution(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        d = a + b
        a = b
        b = d
    
    return int(d % 1234567)
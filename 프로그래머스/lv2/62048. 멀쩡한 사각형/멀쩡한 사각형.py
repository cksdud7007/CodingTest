def gcd(w,h):
    N = min(w,h)
    while (w % N == 0 and h % N == 0) == False:
        N -= 1
    return N, w/N, h/N

def solution(w,h):
    n,a,b = gcd(w,h)
    return w*h - n * (a + b - 1)
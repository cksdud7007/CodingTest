def solution(n,a,b):
    count = 0

    while True:
        if (abs(a-b) == 1 and a//2 != b//2):
            count += 1
            break
        if (a % 2) == 0:
            a = a // 2
        elif (a % 2) != 0:
            a = (a // 2) + 1
        if (b % 2) == 0:
            b = b // 2
        elif (b % 2) != 0:
                b = (b // 2) + 1
        count += 1
    return count
# def solution(N,A,B):
def solution(s):
    count_bin = 0
    count_zero = 0
    while len(s) !=1:
        count_zero += (len(s) - s.count("1"))
        s = s.count("1")
        s = bin(s)[2:]
        count_bin += 1
    return [count_bin,count_zero]
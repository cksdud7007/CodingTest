#import collections
#def solution(clothes):
#    b = []
#    for i in clothes:
#        b.append(i[1])
    
#    b = collections.Counter(b)
#    b = list(b.values())
    
#    for i in range(len(b)):
#        b[i] = b[i] + 1
#    d = 1
#    for i in b:
#        d *= i
#    return d -1


def solution(clothes):
    dict_c = {}
    for i,v in clothes:
        if v in dict_c:
            dict_c[v].append(i)
        else:
            dict_c[v] = [i]
    c_mul = 1
    for i in dict_c.keys():
        c_mul *= (len(dict_c[i]) + 1)
    return c_mul - 1


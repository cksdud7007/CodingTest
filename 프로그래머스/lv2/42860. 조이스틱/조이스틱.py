def solution(name):
    answer = 0
    init_name = 'A' * len(name)
    
    min_step = len(name) - 1
    al_dict = {'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,
               'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,
               'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}
    for i,n in enumerate(name):
        if n != 'A':
            answer += al_dict[n]
        
        check = i + 1
        while check < len(name) and name[check] == 'A':
            check += 1
        min_step = min(2 * i + len(name) - check , min_step, i + 2* (len(name) - check) )
        
    answer += min_step
            
    return answer
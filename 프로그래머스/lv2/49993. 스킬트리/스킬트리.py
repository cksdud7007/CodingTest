def solution(skill, skill_trees):
    skill_number = {}
    result = 0
    for i,v in enumerate(skill):
        skill_number[v] = i
        
    for i in skill_trees:
        answer = []
        idx = 0
        count = 0
        for j in i:
            if j in skill:
                count += 1
                if idx == skill_number[j]:
                    idx += 1
                else:
                    break
        else:
            result += 1
                
    return result
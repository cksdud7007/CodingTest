def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append(i)
        else:
            try:
                answer.pop()
            except:
                return False
    if len(answer):
        return False
    else:
        return True
def solution(s):
    s = s.split(" ")
    answer = []
    for i in s:
        if len(i) == 1:
            answer.append(i.upper())
        elif len(i) == 0:
            answer.append(i)
        else:
            answer.append(i[0].upper() + i[1:].lower())
    return " ".join(answer)
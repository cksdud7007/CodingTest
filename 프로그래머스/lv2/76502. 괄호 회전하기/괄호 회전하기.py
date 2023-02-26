def solution(s):
    count = 0
    for i in range(len(s)):
        answer = []
        renew_s = s[i:] + s[:i]
        for j in renew_s:
            if j in ["(","[","{"]:
                answer.append(j)
            if len(answer)> 0: 
                if (j == ")") and (answer[-1] == "("):
                    answer.pop()
                if j == "]" and ( answer[-1] == "["):
                    answer.pop()
                if j == "}" and (answer[-1] == "{"):
                    answer.pop()
            else:
                answer.append(j)
        if len(answer) == 0:
            count += 1
    return count
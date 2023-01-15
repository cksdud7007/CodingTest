

def solution(number, k):
    number_list = list(number)
    answer= [number_list.pop(0)]
    
    for n in number_list:
        if k > 0:
            while answer[-1] < n:
                answer.pop()
                k -= 1
                if k <= 0 or not answer:
                    break
                
        answer.append(n)
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)
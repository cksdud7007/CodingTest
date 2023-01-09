from collections import deque

def solution(prices):
    answer = []
    que=deque(prices)
    while(que):
        price=que.popleft()
        cnt=0
        for com_price in que : 
            cnt+=1
            if price > com_price :
                break
        answer.append(cnt)

    return answer
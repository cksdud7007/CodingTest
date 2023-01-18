def solution(cards):

    n = len(cards)
    visit = [False] * n # 방문 기록
    answer = []
    
    for idx in range(n): # 상자를 일렬로 순회
        if visit[idx] == False: # 방문 기록 없으면 카드 탐색
            visit[idx] = True
            cnt = 1
            point = cards[idx] - 1
            while True:
                if visit[point] == False:
                    visit[point] = True
                    point = cards[point] - 1
                    cnt += 1   
                else:
                    answer.append(cnt)
                    break
                    
    answer.sort(reverse=True)

    if len(answer) > 1:
        return answer[0] * answer[1]
    else:
        return 0
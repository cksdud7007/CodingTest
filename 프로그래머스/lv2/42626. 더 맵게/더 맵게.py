import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        try:
            heapq.heappush(scoville,heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            answer += 1
        except IndexError:
            return -1
    return answer
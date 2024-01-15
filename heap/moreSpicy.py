# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        curSco = heapq.heappop(scoville)
        if curSco >= K:
            break
        if len(scoville) == 0:
            return -1
        secSco = heapq.heappop(scoville)
        heapq.heappush(scoville, curSco + secSco * 2)

        answer += 1

    return answer


print(solution([2, 3], 7))
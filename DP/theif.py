# https://school.programmers.co.kr/learn/courses/30/lessons/42897
import copy
from collections import deque


def solution(money):
    global firstSelect
    N = len(money)
    vList = [0]*N

    def dfs(idx, totalMoney):
        if N-2 <= idx:
            print(vList)
            print(totalMoney)
            return totalMoney

        maxTmp = 0
        for i in range(idx+2, idx+5):
            if i >= N:
                continue
            prev = i-1
            next = i+1
            if prev < 0:
                prev = N - 1
            elif next == N:
                next = 0

            if vList[i] == 0 and vList[prev] == 0 and vList[next] == 0:
                vList[i] = 1
                maxTmp = max(maxTmp, dfs(i, totalMoney + money[i]))
                vList[i] = 0

        return maxTmp

    maxMoney = 0
    for j in range(0, 3):
        vList[j] = 1
        maxMoney = max(maxMoney, dfs(j, money[j]))
        vList[j] = 0

    return maxMoney

# print(solution([1, 1, 4, 1, 4]))
print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]))





# cache = [[-1]*2 for _ in range(N)]
#
#     def dp(idx):
#         global firstSelect
#         if idx >= N:
#             return 0
#         if idx == N - 1 and firstSelect:
#             return 0
#
#         ret = cache[idx][firstSelect]
#         if ret != -1:
#             return ret
#
#         if idx == 0:
#             firstSelect = 1
#         ret = max(ret, money[idx] + dp(idx + 2))
#         if idx == 0:
#             firstSelect = 0
#         ret = max(ret, dp(idx+1))
#
#         return ret
#
#     firstSelect = 0
#     maxMoney = dp(0)
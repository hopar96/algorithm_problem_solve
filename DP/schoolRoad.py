# https://school.programmers.co.kr/learn/courses/30/lessons/42898
from collections import deque


def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for l in puddles:
        dp[l[1]][l[0]] = -1

    dp[1][1] = 1
    for y in range(1, n+1):
        for x in range(1, m+1):
            print((x, y))
            if x == 1 and y == 1:
                dp[y][x] = 1
                continue
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            tmp1 = 0
            tmp2 = 0
            if y-1 > 0:
                print('y-1 > 0')
                tmp1 = dp[y-1][x]
            if x-1 > 0:
                print('x-1 > 0')
                tmp2 = dp[y][x - 1]
            print('x, y : ', (x, y))
            print((tmp1, tmp2))
            dp[y][x] = tmp1 + tmp2

    print(dp)
    return dp[n][m] % 1000000007

print(solution(4, 3, [[2, 2]]))



# dfs 풀이 효율성 탈락
# def dfs(x, y):
#     if x == 1 and y == 1:
#         return 1
#
#     tmp1 = 0
#     tmp2 = 0
#     if 0 < x - 1 and vList[y][x - 1] == 0:
#         vList[y][x - 1] = 1
#         tmp1 = dfs(x - 1, y)
#         vList[y][x - 1] = 0
#
#     if 0 < y - 1 and vList[y - 1][x] == 0:
#         vList[y - 1][x] = 1
#         tmp2 = dfs(x, y - 1)
#         vList[y - 1][x] = 0
#
#     return tmp1 + tmp2
#
#
# return dfs(m, n) % 1000000007


# BFS 풀이 효율성 탈락

#  cnt = 0
#     que = deque()
#     que.append((m, n))
#     while que:
#         curX, curY = que.popleft()
#         if curY == 1 and curX == 1:
#             cnt += 1
#
#         for nx, ny in dList:
#             nextY = curY + ny
#             nextX = curX + nx
#
#             if 0 < nextX and 0 < nextY and vList[nextY][nextX] == 0:
#                 que.append((nextX, nextY))
#
#     return cnt % 1000000007
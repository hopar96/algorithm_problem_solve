# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    dirList = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동서남북
    xRange = len(maps[0])
    yRange = len(maps)
    vList = [[0] * xRange for _ in range(yRange)]

    que = deque()
    que.append((0, 0, 1))
    vList[0][0] = 1
    answer = -1
    while que:
        curX, curY, curCnt = que.popleft()
        if curX == xRange-1 and curY == yRange-1:
            answer = curCnt
            break

        for dx, dy in dirList:
            nextX = curX + dx
            nextY = curY + dy
            if 0 <= nextX < xRange and 0 <= nextY < yRange:
                if maps[nextY][nextX] != 0:
                    if vList[nextY][nextX] == 0:
                        vList[nextY][nextX] = 1
                        que.append((nextX, nextY, curCnt + 1))

    return answer


# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

#
# def solution(maps):
#     dirList = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동서남북
#
#     xRange = len(maps[0])
#     yRange = len(maps)
#     vList = [[0] * xRange for _ in range(yRange)]
#     limit = xRange * yRange
#     def dfs(cnt, xy):
#         x, y = xy
#         if x == xRange-1 and y == yRange-1:
#             return cnt
#
#         answer = limit
#         for dx, dy in dirList:
#             if 0 <= x + dx < xRange and 0 <= y + dy < yRange:
#                 if maps[y + dy][x + dx] != 0:
#                     if vList[y + dy][x + dx] == 0:
#                         vList[y + dy][x + dx] = 1
#                         answer = min(answer, dfs(cnt + 1, (x + dx, y + dy)))
#                         vList[y + dy][x + dx] = 0
#
#         return answer
#
#     answer = dfs(1, (0, 0))
#     if answer == limit:
#         return -1
#     return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[' ']*153 for _ in range(153)]
    idx = 0
    for fX, fY, sX, sY in rectangle:
        idx += 1
        for x in range(fX*3+1, (sX+1)*3-1):
            for y in range(fY*3+1, (sY+1)*3-1):
                board[y][x] = 1

    # 안에 공간 빼기
    for fX, fY, sX, sY in rectangle:
        for x in range((fX+1)*3-1, sX*3+1):
            for y in range((fY+1)*3-1, sY*3+1):
                board[y][x] = ' '

    print(0, [str(j%10) for j in range(0, 102)])
    for idx, i in enumerate(board):
        print(idx,i)

    dList = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    que = deque()
    que.append((characterX*3+1, characterY*3+1, 0, 0, -1, 5))
    while que:
        curX, curY, cnt, eCnt, prevEdge, prevIdx = que.popleft()
        print((curX, curY, cnt, eCnt, prevEdge))
        if curX == itemX*3+1 and curY == itemY*3+1:
            return int(cnt/3)

        for idx, item in enumerate(dList):
            nextX = curX + item[0]
            nextY = curY + item[1]
            noIdx = prevIdx+1 if prevIdx % 2 == 0 else prevIdx-1
            if idx != noIdx and board[nextY][nextX] == 1:
                if (prevEdge == 0 and idx > 1) or (prevEdge == 1 and idx < 2):
                    eCnt += 1

                que.append((nextX, nextY, cnt+1, eCnt, int(idx > 1), idx))

    return answer


# print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))

(2, 8, 0, 0, -1)
# board = [[' ']*51 for _ in range(51)]
#
#     idx = 0
#     for fX, fY, sX, sY in rectangle:
#         idx+=1
#         for x in range(fX, sX+1):
#             for y in range(fY, sY+1):
#                 board[y][x] = str(idx)
#
#     # 안에 공간 빼기
#     for fX, fY, sX, sY in rectangle:
#         # if sX - fX > 2 and sY - fY > 2:
#         for x in range(fX+1, sX):
#             for y in range(fY+1, sY):
#                 board[y][x] = ' '
#
#     print(0, [str(j) for j in range(0, 51)])
#     for idx, i in  enumerate(board):
#         print(idx,i)


# board = [[' '] * 153 for _ in range(153)]
# idx = 0
# for fX, fY, sX, sY in rectangle:
#     idx += 1
#     for x in range(fX * 3 + 1, (sX + 1) * 3 - 1):
#         for y in range(fY * 3 + 1, (sY + 1) * 3 - 1):
#             board[y][x] = str(idx)
#
# # 안에 공간 빼기
# for fX, fY, sX, sY in rectangle:
#     # if sX - fX > 2 and sY - fY > 2:
#     for x in range((fX + 1) * 3 - 1, sX * 3 + 1):
#         for y in range((fY + 1) * 3 - 1, sY * 3 + 1):
#             board[y][x] = ' '
#
# print(0, [str(j) for j in range(0, 102)])
# for idx, i in enumerate(board):
#     print(idx, i)
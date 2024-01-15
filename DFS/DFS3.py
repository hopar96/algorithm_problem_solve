# 백준 1987번 문제

# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
#
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
#
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.
from collections import deque

def dfs(board, x, y):
   ans = 1
   q = set([(x, y, board[y][x])])
   while q:
      x, y, alpha = q.pop()
      ans = max(ans, len(alpha))

      for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in alpha:
            q.add((nx, ny, alpha + board[ny][nx]))

   return ans
# main
rc = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
R = rc[0]
C = rc[1]

board = [list(input()) for _ in range(R)]
print(dfs(board, 0, 0))

# board2 = [[False for _ in range(C+2)] for _ in range(R+2)]
# for y in range(len(board)):
#    for x in range(len(board[y])):
#       board2[y+1][x+1] = board[y][x]

# for d in DList:
#    if 0 <= (y + d[0]) < R and 0 <= (x + d[1]) < C:  # board 범위
#       if tListLen != len(set(tList + [board[y+d[0]][x+d[1]]])):
#          endFlg = False
#          dfs([y+d[0], x+d[1]], tList + [board[y+d[0]][x+d[1]]])

# def dfs(curLoc, tDic):
#    global ans, R, C
#    y = curLoc[0]
#    x = curLoc[1]
#    tLen = len(tDic)
#    endFlg = True
#
#    for d in DList:
#       if board2[y+d[0]][x+d[1]] != False and board2[y+d[0]][x+d[1]] not in tDic:
#          endFlg = False
#          tDic[board2[y + d[0]][x + d[1]]] = True
#          dfs([y+d[0], x+d[1]], tDic)
#          del tDic[board2[y + d[0]][x + d[1]]]
#
#    if endFlg:
#       ans = max(tLen, ans)
#       return
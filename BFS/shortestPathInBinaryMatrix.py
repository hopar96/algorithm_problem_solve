# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
from collections import deque


def shortestPathBinaryMatrix(grid):
    row = len(grid)
    col = len(grid[0])
    pathLen = -1

    if grid[0][0] == 1 or grid[row-1][col-1]:
        return pathLen

    visited = [[False]*col for _ in range(row)]
    dirX = [1, 1, 1, -1, -1, -1, 0, 0]
    dirY = [0, -1, 1, 0, 1, -1, 1, -1]

    def bfs(r, c):
        queue = deque()
        queue.append((r, c, 0))

        while queue:
            tmpY, tmpX, tmpLen = queue.popleft()
            if tmpY == row - 1 and tmpX == col - 1:
                return tmpLen+1
            visited[tmpY][tmpX] = True
            for i in range(8):
                targetX = tmpX + dirX[i]
                targetY = tmpY + dirY[i]
                if 0 <= targetY < row and 0 <= targetX < col:
                    if not visited[targetY][targetX] and grid[targetY][targetX] == 0:
                        visited[targetY][targetX] = True
                        queue.append((targetY, targetX, tmpLen+1))

        return -1



    pathLen = bfs(0, 0)
    return pathLen



print(shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
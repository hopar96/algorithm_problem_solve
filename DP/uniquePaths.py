# https://leetcode.com/problems/unique-paths/description/

def uniquePaths(m, n):

    pathCnt = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 2}

    def dfs(y, x):
        if y < 2 and x < 2:
            return pathCnt.get((y, x))

        fCnt = 0
        sCnt = 0
        if 0 <= y - 1 < m:
            if (y-1, x) in pathCnt:
                fCnt = pathCnt.get((y-1, x))
            else:
                fCnt = dfs(y-1, x)
        if 0 <= x - 1 < n:
            if (y, x-1) in pathCnt:
                sCnt = pathCnt.get((y, x-1))
            else:
                sCnt = dfs(y, x-1)
        pathCnt[(y, x)] = fCnt + sCnt
        return pathCnt[(y, x)]
    dfs(m-1, n-1)
    print(pathCnt)
    return pathCnt.get((m-1, n-1))


print(uniquePaths(3, 2))

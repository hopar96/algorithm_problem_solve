# 백준 1199 문제


# 어느 점에서 출발하여 그래프 상에 있는 모든 간선을 지나되 한번 지난 간선은 다시 지나지 않고 출발점으로 돌아오는 회로를 오일러 회로라 한다. 단, 그래프는 양방향 그래프가 주어진다.
#
# 문제는 그래프가 주어졌을 때 오일러 회로 경로를 출력하는 것이다.
import sys
sys.setrecursionlimit(10**6)

def dfs(tList):
    global ans, lineCnt, endFlg
    if endFlg:
        return
    curNode = tList[len(tList) - 1]
    if len(tList) == lineCnt+1:
        if tList[0] == curNode:
            ans = tList
            endFlg = True

        return


    for i in range(len(list[curNode])):
        if list[curNode][i] > 0 and not endFlg:
            list[curNode][i] -= 1
            list[i][curNode] -= 1
            dfs(tList + [i])
            list[curNode][i] += 1
            list[i][curNode] += 1

N = int(input())
list = [list(map(int, input().split())) for _ in range(N)]
lineCnt = 0
for i in list:
    for j in i:
       lineCnt += int(j)

lineCnt = int(lineCnt / 2)
ans = -1
endFlg = False
for i in range(N):
    if not endFlg:
        dfs([i])
if ans.__class__ == int:
    print(ans)
else:
    tmp = ''
    for i in range(len(ans)):
        tmp += str(ans[i] + 1)
        if i != len(ans)-1:
            tmp += ' '
    print(tmp)



# 7576번 문제
# https://www.acmicpc.net/problem/7576

# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.
#
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며,
# 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지,그 최소 일수를 구하는 프로그램을 작성하라.
# 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

mn = list(map(int, input().split()))
M = mn[0]
N = mn[1]

tomatoBox = [list(map(int, input().split())) for _ in range(N)]
day = 0
ripedCnt = 0
rawCnt = 0
totCnt = 0
ripedTomatoQue = []
ripeLoc = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for y in range(N):
    for x in range(M):
        curLocStat = tomatoBox[y][x]
        if curLocStat == 1:
            ripedCnt += 1
            ripedTomatoQue.append([x, y])
        if curLocStat != -1:
            totCnt += 1

while ripedTomatoQue:
    newRipedList = []
    if ripedCnt == totCnt:
        print(day)
        break
    day += 1
    for x, y in ripedTomatoQue:
        for x2, y2 in ripeLoc:
            y_ = y + y2
            x_ = x + x2
            if 0 <= y_ < N and 0 <= x_ < M:
                if tomatoBox[y_][x_] == 0:
                    tomatoBox[y_][x_] = 1
                    ripedCnt += 1
                    newRipedList.append([x_, y_])
        if ripedCnt == totCnt:
            break
    if len(newRipedList) == 0:
        print(-1)
        break
    ripedTomatoQue = newRipedList


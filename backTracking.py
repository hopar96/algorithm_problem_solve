from collections import deque


# 1987번 문제
# https://www.acmicpc.net/problem/1987

# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

def nextRoute (x, y, route, alpha):

    if x-1 >= 0:
        if route.count(alpha[x - 1][y]) == 0:
            nextRoute(x-1, y, route.append([x, y]), alpha)
    # if alpha[x + 1][y]:
        # todo




rc = list(map(int, input().split()))
R = rc[0]
C = rc[1]

alphabet = [list(map(int, input().split())) for _ in range(R)]

route = []
